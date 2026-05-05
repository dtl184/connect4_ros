#!/usr/bin/env python3

import copy
import time
import math
import threading

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from moveit_msgs.action import MoveGroup
from std_srvs.srv import Empty

from connect4_msgs.action import PickAndPlace


class PickAndPlaceActionServer(Node):
    def __init__(self):
        super().__init__("pick_and_place_action_server")

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

        self.action_server = ActionServer(
            self,
            PickAndPlace,
            "/connect4/pick_and_place",
            execute_callback=self.execute_callback,
            callback_group=self.cb_group,
        )

        # Tune these carefully.
        self.hover_z = 0.100
        self.pick_z = 0.015
        self.place_z = 0.020

        # Descend in steps like your working PickAndDrop server.
        self.pick_descend_steps = [0.075, 0.065, 0.055, self.pick_z]
        self.place_descend_steps = [0.075, 0.060, 0.045, self.place_z]

        self.get_logger().info("PickAndPlace action server ready")

    def execute_callback(self, goal_handle):
        result = PickAndPlace.Result()

        try:
            ok, msg = self.pick_and_place(goal_handle)
            result.success = ok
            result.message = msg

            if ok:
                goal_handle.succeed()
            else:
                goal_handle.abort()

            return result

        except Exception as e:
            self.get_logger().exception("Pick-and-place failed")
            result.success = False
            result.message = str(e)
            goal_handle.abort()
            return result

    
    def make_drop_pose(self):
        pose = PoseStamped()
        pose.header.frame_id = "base_link"

        pose.pose.position.x = 0.242
        pose.pose.position.y = -0.379
        pose.pose.position.z = 0.094

        pose.pose.orientation.x = -0.759
        pose.pose.orientation.y = 0.650
        pose.pose.orientation.z = -0.018
        pose.pose.orientation.w = 0.039

        self.normalize_quaternion(pose)
        return pose


    def pick_and_place(self, goal_handle):
        pickup_hover = copy.deepcopy(goal_handle.request.pickup_pose)
        place_hover = copy.deepcopy(goal_handle.request.place_pose)

        # Treat incoming poses as XY hover targets.
        pickup_hover.header.frame_id = "base"
        place_hover.header.frame_id = "base"

        pickup_hover.pose.position.z = self.hover_z
        place_hover.pose.position.z = self.hover_z

        self.set_gripper_orientation(pickup_hover)
        self.set_gripper_orientation(place_hover)

        self.publish_feedback(goal_handle, "Opening gripper narrowly")
        if not self.open_gripper_narrow():
            return False, "Failed to narrow-open gripper"

        self.publish_feedback(goal_handle, "Moving to pickup hover")
        if not self.move_to_pose(pickup_hover, "pickup hover"):
            return False, "Failed to move to pickup hover"

        self.publish_feedback(goal_handle, "Descending to pickup")
        for i, z in enumerate(self.pick_descend_steps):
            p = copy.deepcopy(pickup_hover)
            p.pose.position.z = z
            if not self.move_to_pose(p, f"pickup descend step {i}"):
                return False, f"Failed during pickup descend step {i}"

        self.publish_feedback(goal_handle, "Closing gripper")
        if not self.close_gripper():
            return False, "Failed to close gripper"

        time.sleep(1.5)

        self.publish_feedback(goal_handle, "Lifting block")
        if not self.move_to_pose(pickup_hover, "lift from pickup"):
            return False, "Failed to lift block"

        self.publish_feedback(goal_handle, "Moving to place hover")
        if not self.move_to_pose(place_hover, "place hover"):
            return False, "Failed to move to place hover"

        self.publish_feedback(goal_handle, "Descending to place")
        for i, z in enumerate(self.place_descend_steps):
            p = copy.deepcopy(place_hover)
            p.pose.position.z = z
            if not self.move_to_pose(p, f"place descend step {i}"):
                return False, f"Failed during place descend step {i}"

        self.publish_feedback(goal_handle, "Opening gripper at place location")
        if not self.open_gripper():
            return False, "Failed to open gripper at place location"

        time.sleep(0.5)


        final_pose = self.make_drop_pose()
        self.publish_feedback(goal_handle, "Retreating from placed block")
        if not self.move_to_pose(final_pose, "retreat from place"):
            return False, "Failed to retreat after placing"

        self.publish_feedback(goal_handle, "Pick and place complete")
        return True, "Pick and place complete"

    def set_gripper_orientation(self, pose: PoseStamped):
        # Same orientation as your working PickAndDrop make_pose().
        pose.pose.orientation.x = -0.012
        pose.pose.orientation.y = 1.000
        pose.pose.orientation.z = 0.021
        pose.pose.orientation.w = 0.014
        self.normalize_quaternion(pose)
    


    def publish_feedback(self, goal_handle, status: str):
        feedback = PickAndPlace.Feedback()
        feedback.status = status
        goal_handle.publish_feedback(feedback)
        self.get_logger().info(status)

    def wait_for_future(self, future, timeout_sec=None):
        event = threading.Event()
        future.add_done_callback(lambda _: event.set())
        ok = event.wait(timeout=timeout_sec)
        if not ok:
            return None
        return future.result()

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
        self.get_logger().info(
            f"Moving to {label}: "
            f"x={pose.pose.position.x:.3f}, "
            f"y={pose.pose.position.y:.3f}, "
            f"z={pose.pose.position.z:.3f}"
        )

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

    def normalize_quaternion(self, pose):
        q = pose.pose.orientation
        norm = math.sqrt(q.x*q.x + q.y*q.y + q.z*q.z + q.w*q.w)

        q.x /= norm
        q.y /= norm
        q.z /= norm
        q.w /= norm


def main(args=None):
    rclpy.init(args=args)

    node = PickAndPlaceActionServer()
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()