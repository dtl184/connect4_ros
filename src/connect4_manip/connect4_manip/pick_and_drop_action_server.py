#!/usr/bin/env python3

import time
import math
import threading
from typing import Optional

import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from moveit_msgs.action import MoveGroup
from std_srvs.srv import Empty

from connect4_msgs.action import PickAndDrop


class PickAndDropActionServer(Node):
    def __init__(self):
        super().__init__("pick_and_drop_action_server")

        self.cb_group = ReentrantCallbackGroup()

        self.move_client = ActionClient(
            self,
            MoveGroup,
            "/move_action",
            callback_group=self.cb_group,
        )

        self.gripper_close_client = self.create_client(
            Empty,
            "/connect4/gripper/close",
            callback_group=self.cb_group,
        )

        self.gripper_open_client = self.create_client(
            Empty,
            "/connect4/gripper/open",
            callback_group=self.cb_group,
        )

        self.gripper_open_narrow_client = self.create_client(
            Empty,
            "/connect4/gripper/open_narrow",
            callback_group=self.cb_group,
        )

        self.latest_block_pose: Optional[PoseStamped] = None

        self.block_pose_sub = self.create_subscription(
            PoseStamped,
            "/detected_block_pose",
            self.block_pose_callback,
            10,
            callback_group=self.cb_group,
        )

        self.action_server = ActionServer(
            self,
            PickAndDrop,
            "/connect4/pick_and_drop",
            execute_callback=self.execute_callback,
            callback_group=self.cb_group,
        )

        self.get_logger().info("PickAndDrop action server ready")

    def block_pose_callback(self, msg: PoseStamped):
        self.latest_block_pose = msg

    def wait_for_future(self, future, timeout_sec=None):
        event = threading.Event()
        future.add_done_callback(lambda _: event.set())
        ok = event.wait(timeout=timeout_sec)
        if not ok:
            return None
        return future.result()

    def publish_feedback(self, goal_handle, status: str):
        feedback = PickAndDrop.Feedback()
        feedback.status = status
        goal_handle.publish_feedback(feedback)
        self.get_logger().info(status)

    def execute_callback(self, goal_handle):
        result = PickAndDrop.Result()

        try:
            ok, msg = self.pick_and_drop(goal_handle)
            result.success = ok
            result.message = msg

            if ok:
                goal_handle.succeed()
            else:
                goal_handle.abort()

            return result

        except Exception as e:
            self.get_logger().exception("Pick-and-drop failed")
            result.success = False
            result.message = str(e)
            goal_handle.abort()
            return result

    def pick_and_drop(self, goal_handle):
        self.publish_feedback(goal_handle, "Waiting for detected block pose")
        block_pose = self.wait_for_block_pose(timeout_sec=10.0)

        if block_pose is None:
            return False, "Timed out waiting for /detected_block_pose"

        raw_x = block_pose.pose.position.x
        raw_y = block_pose.pose.position.y

        self.get_logger().info(f"RAW block pose: x={raw_x:.4f}, y={raw_y:.4f}")

        block_x, block_y = self.raw_block_to_base(raw_x, raw_y)

        block_y += -0.006
        block_x += 0.011

        if 0.095 <= raw_x <= 0.13 and 0.015 <= raw_y <= 0.05:
            self.get_logger().warn("Applying correction for Mid-Right")
            block_x += 0.01
            block_y += 0.0

        self.get_logger().info(f"BASE block pose: x={block_x:.4f}, y={block_y:.4f}")

        above_z = 0.085
        grasp_z = above_z - 0.075

        above_pose = self.make_pose(block_x, block_y, above_z)

        self.publish_feedback(goal_handle, "Opening gripper narrowly")
        if not self.open_gripper_narrow():
            return False, "Failed to narrow-open gripper"

        self.publish_feedback(goal_handle, "Moving above block")
        if not self.move_to_pose(above_pose, "above block"):
            return False, "Failed to move above block"

        self.publish_feedback(goal_handle, "Descending to block")
        for i, z in enumerate([0.075, 0.065, 0.055, grasp_z]):
            p = self.make_pose(block_x, block_y, z)
            if not self.move_to_pose(p, f"descend step {i}"):
                return False, f"Failed during descend step {i}"

        self.publish_feedback(goal_handle, "Closing gripper")
        if not self.close_gripper():
            return False, "Failed to close gripper"

        time.sleep(1.5)

        self.publish_feedback(goal_handle, "Lifting block")
        if not self.move_to_pose(above_pose, "lift"):
            return False, "Failed to lift block"

        self.publish_feedback(goal_handle, "Moving to drop pose")
        drop_pose = self.make_drop_pose()
        if not self.move_to_pose(drop_pose, "drop pose"):
            return False, "Failed to move to drop pose"

        self.publish_feedback(goal_handle, "Opening gripper fully at drop area")
        if not self.open_gripper():
            return False, "Failed to open gripper at drop area"

        time.sleep(0.5)

        self.publish_feedback(goal_handle, "Pick and drop complete")
        return True, "Pick and drop complete"

    def make_drop_pose(self):
        pose = PoseStamped()
        pose.header.frame_id = "base"

        pose.pose.position.x = 0.242
        pose.pose.position.y = -0.379
        pose.pose.position.z = 0.094

        pose.pose.orientation.x = -0.759
        pose.pose.orientation.y = 0.650
        pose.pose.orientation.z = -0.018
        pose.pose.orientation.w = 0.039

        self.normalize_quaternion(pose)
        return pose

    def wait_for_block_pose(self, timeout_sec=10.0):
        start = time.time()

        while rclpy.ok() and self.latest_block_pose is None:
            if time.time() - start > timeout_sec:
                self.get_logger().error("Timed out waiting for /detected_block_pose")
                return None
            time.sleep(0.05)

        return self.latest_block_pose

    def raw_block_to_base(self, raw_x, raw_y):
        calibration = np.array([
            [0.115, 0.108, -0.056, -0.439],
            [0.113, 0.047, -0.068, -0.385],
            [0.111, 0.171, -0.058, -0.488],
            [0.044, 0.111, -0.104, -0.437],
            [0.047, 0.047, -0.116, -0.385],
            [0.047, 0.170, -0.102, -0.492],
            [0.180, 0.106,  0.005, -0.435],
            [0.181, 0.046,  0.006, -0.379],
            [0.180, 0.170,  0.005, -0.490],
        ], dtype=float)

        rx = calibration[:, 0]
        ry = calibration[:, 1]
        bx = calibration[:, 2]
        by = calibration[:, 3]

        A = np.column_stack([
            rx,
            ry,
            rx * ry,
            rx * rx,
            ry * ry,
            np.ones_like(rx),
        ])

        coeff_x, _, _, _ = np.linalg.lstsq(A, bx, rcond=None)
        coeff_y, _, _, _ = np.linalg.lstsq(A, by, rcond=None)

        x = raw_x
        y = raw_y

        features = np.array([
            x,
            y,
            x * y,
            x * x,
            y * y,
            1.0,
        ])

        base_x = float(features @ coeff_x)
        base_y = float(features @ coeff_y)

        return base_x, base_y

    def make_pose(self, x, y, z):
        pose = PoseStamped()
        pose.header.frame_id = "base"

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        pose.pose.orientation.x = -0.012
        pose.pose.orientation.y = 1.000
        pose.pose.orientation.z = 0.021
        pose.pose.orientation.w = 0.014

        self.normalize_quaternion(pose)
        return pose

    def normalize_quaternion(self, pose):
        q = pose.pose.orientation
        norm = math.sqrt(q.x*q.x + q.y*q.y + q.z*q.z + q.w*q.w)

        q.x /= norm
        q.y /= norm
        q.z /= norm
        q.w /= norm

    def call_empty_service(self, client, name):
        self.get_logger().info(f"Waiting for {name} service")

        if not client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error(f"{name} service not available")
            return False

        future = client.call_async(Empty.Request())
        response = self.wait_for_future(future, timeout_sec=10.0)

        if response is None:
            self.get_logger().error(f"{name} service call failed or timed out")
            return False

        return True

    def close_gripper(self):
        return self.call_empty_service(self.gripper_close_client, "gripper close")

    def open_gripper(self):
        return self.call_empty_service(self.gripper_open_client, "gripper full open")

    def open_gripper_narrow(self):
        return self.call_empty_service(
            self.gripper_open_narrow_client,
            "gripper narrow open"
        )

    def move_to_pose(self, pose, label="pose"):
        self.get_logger().info(f"Moving to {label}")

        if not self.move_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error("MoveIt /move_action server not available")
            return False

        goal = MoveGroup.Goal()
        goal.request.group_name = "ur_manipulator"
        goal.request.goal_constraints.append(self.pose_to_constraints(pose))
        goal.request.max_velocity_scaling_factor = 0.05
        goal.request.max_acceleration_scaling_factor = 0.05

        send_future = self.move_client.send_goal_async(goal)
        goal_handle = self.wait_for_future(send_future, timeout_sec=10.0)

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error(f"Move goal rejected: {label}")
            return False

        result_future = goal_handle.get_result_async()
        result = self.wait_for_future(result_future, timeout_sec=60.0)

        if result is None:
            self.get_logger().error(f"Move timed out: {label}")
            return False

        error_code = result.result.error_code.val

        if error_code != 1:
            self.get_logger().error(
                f"Move failed: {label}, MoveIt error code {error_code}"
            )
            return False

        return True

    def pose_to_constraints(self, pose):
        from moveit_msgs.msg import Constraints, PositionConstraint, OrientationConstraint
        from shape_msgs.msg import SolidPrimitive

        constraints = Constraints()

        pc = PositionConstraint()
        pc.header = pose.header
        pc.link_name = "tool0"

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.01, 0.01, 0.01]

        pc.constraint_region.primitives.append(box)
        pc.constraint_region.primitive_poses.append(pose.pose)
        pc.weight = 1.0

        oc = OrientationConstraint()
        oc.header = pose.header
        oc.link_name = "tool0"
        oc.orientation = pose.pose.orientation
        oc.absolute_x_axis_tolerance = 0.01
        oc.absolute_y_axis_tolerance = 0.01
        oc.absolute_z_axis_tolerance = 0.01
        oc.weight = 1.0

        constraints.position_constraints.append(pc)
        constraints.orientation_constraints.append(oc)

        return constraints


def main(args=None):
    rclpy.init(args=args)

    node = PickAndDropActionServer()
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()