#!/usr/bin/env python3

import time
import math
from typing import Optional

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped
from moveit_msgs.action import MoveGroup
from std_srvs.srv import Empty


class MoveItPoseClient(Node):
    def __init__(self):
        super().__init__("moveit_pose_client")

        self.client = ActionClient(self, MoveGroup, "/move_action")

        self.gripper_close_client = self.create_client(
            Empty,
            "/connect4/gripper/close"
        )

        self.gripper_open_client = self.create_client(
            Empty,
            "/connect4/gripper/open"
        )

        self.latest_block_pose: Optional[PoseStamped] = None

        self.block_pose_sub = self.create_subscription(
            PoseStamped,
            "/detected_block_pose",
            self.block_pose_callback,
            10,
        )

    def block_pose_callback(self, msg: PoseStamped):
        self.latest_block_pose = msg

    # -----------------------------
    # GRIPPER
    # -----------------------------
    def call_empty_service(self, client, name):
        self.get_logger().info(f"Waiting for {name} service...")

        if not client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error(f"{name} service not available")
            return False

        req = Empty.Request()
        future = client.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is None:
            self.get_logger().error(f"{name} service call failed")
            return False

        return True

    def close_gripper(self):
        return self.call_empty_service(self.gripper_close_client, "gripper close")

    def open_gripper(self):
        return self.call_empty_service(self.gripper_open_client, "gripper open")

    # -----------------------------
    # CALIBRATED MAPPING (NO TF)
    # -----------------------------
    def raw_block_to_base(self, raw_x, raw_y):
        import numpy as np

        calibration = np.array([
            [0.115, 0.108, -0.056, -0.439],  # CENTER
            [0.113, 0.047, -0.068, -0.385],  # MID_RIGHT
            [0.111, 0.171, -0.058, -0.488],  # MID_LEFT

            [0.044, 0.111, -0.104, -0.437],  # TOP_CENTER
            [0.047, 0.047, -0.116, -0.385],  # TOP_RIGHT
            [0.047, 0.170, -0.102, -0.492],  # TOP_LEFT

            [0.180, 0.106,  0.005, -0.435],  # BOTTOM_CENTER
            [0.181, 0.046,  0.006, -0.379],  # BOTTOM_RIGHT
            [0.180, 0.170,  0.005, -0.490],  # BOTTOM_LEFT
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
    def wait_for_block_pose(self, timeout_sec=10.0):
        self.get_logger().info("Waiting for /detected_block_pose...")

        start = time.time()
        while rclpy.ok() and self.latest_block_pose is None:
            rclpy.spin_once(self, timeout_sec=0.1)

            if time.time() - start > timeout_sec:
                self.get_logger().error("Timed out waiting for detected block pose")
                return None

        return self.latest_block_pose

    # -----------------------------
    # POSE UTILS
    # -----------------------------
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

    # -----------------------------
    # MOVEIT
    # -----------------------------
    def move_to_pose(self, pose, label="pose"):
        self.client.wait_for_server()

        goal = MoveGroup.Goal()
        goal.request.group_name = "ur_manipulator"
        goal.request.goal_constraints.append(self.pose_to_constraints(pose))

        goal.request.max_velocity_scaling_factor = 0.05
        goal.request.max_acceleration_scaling_factor = 0.05

        future = self.client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, future)

        goal_handle = future.result()

        if not goal_handle or not goal_handle.accepted:
            self.get_logger().error(f"Move failed: {label}")
            return False

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

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

    # -----------------------------
    # PICK PIPELINE
    # -----------------------------
    def pick_block(self):
        self.latest_block_pose = None

        block_pose = self.wait_for_block_pose()
        if block_pose is None:
            return

        raw_x = block_pose.pose.position.x
        raw_y = block_pose.pose.position.y

        self.get_logger().info(f"RAW: {raw_x:.4f}, {raw_y:.4f}")

        # 🔥 USE CALIBRATED MAPPING
        block_x, block_y = self.raw_block_to_base(raw_x, raw_y)

        block_y += -0.006
        self.get_logger().info(f"BASE: {block_x:.4f}, {block_y:.4f}")

        above_z = 0.085
        grasp_z = above_z - 0.075

        above_pose = self.make_pose(block_x, block_y, above_z)
        grasp_pose = self.make_pose(block_x, block_y, grasp_z)

        if not self.open_gripper():
            return

        if not self.move_to_pose(above_pose, "above block"):
            return
        
        

        for i, z in enumerate([0.075, 0.065, 0.055, grasp_z]):
            p = self.make_pose(block_x, block_y, z)
            if not self.move_to_pose(p, f"descend step {i}"):
                return

        if not self.close_gripper():
            return

        time.sleep(1.5)

        if not self.move_to_pose(above_pose, "lift"):
            return

        self.get_logger().info("Pick complete")

def main():
    rclpy.init()
    node = MoveItPoseClient()
    node.pick_block()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()