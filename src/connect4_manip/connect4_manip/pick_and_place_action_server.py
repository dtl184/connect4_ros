#!/usr/bin/env python3

"""
Pick-And-Place action server 

This node:
    1. Receives pickup and placement poses.
    2. Uses MoveIt to move the UR arm.
    3. Picks a block from pickup pose and places it at placement pose.


ROS Interfaces
--------------
ACTION SERVER:
    /connect4/pick_and_place
        Type: connect4_msgs/action/PickAndPlace

Gripper Services:
    /connect4/gripper/open
    /connect4/gripper/open_narrow
    /connect4/gripper/close
        Type: std_srvs/srv/Empty

MOVEIT ACTION CLIENT:
    /move_action
        Type: moveit_msgs/action/MoveGroup
"""

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
    """
    Action server responsible for pick-and-place operations during player mode.

    """

    def __init__(self):
        super().__init__("pick_and_place_action_server")

        self.cb_group = ReentrantCallbackGroup()

        # MoveIt action client
        self.move_client = ActionClient(
            self,
            MoveGroup,
            "/move_action",
            callback_group=self.cb_group,
        )

        # Gripper service clients

        # Close gripper
        self.gripper_close_client = self.create_client(
            Empty,
            "/connect4/gripper/close",
            callback_group=self.cb_group,
        )

        # Open gripper
        self.gripper_open_narrow_client = self.create_client(
            Empty,
            "/connect4/gripper/open_narrow",
            callback_group=self.cb_group,
        )

        # Pick-and-place action server
        self.action_server = ActionServer(
            self,
            PickAndPlace,
            "/connect4/pick_and_place",
            execute_callback=self.execute_callback,
            callback_group=self.cb_group,
        )

        # Motion parameters

        # Hover height above pickup/place locations
        self.hover_z = 0.100

        # Final pickup height
        self.pick_z = 0.015

        # Final placement height
        self.place_z = 0.020

        # Incremental pickup descent heights
        self.pick_descend_steps = [
            0.075,
            0.065,
            0.055,
            self.pick_z,
        ]

        # Incremental placement descent heights
        self.place_descend_steps = [
            0.075,
            0.060,
            0.045,
            self.place_z,
        ]

        # Rest pose
        # I make the robot go here after placing because sometimes MoveIt! sends a 
        # weird trajectory to pickup the next block, if it goes here first it's a lot better
        self.rest_x = -0.081
        self.rest_y = -0.417
        self.rest_z = 0.210

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

    def make_rest_pose(self):
        """
        Create the robot rest pose.
        """
        pose = PoseStamped()

        pose.header.frame_id = "base"

        pose.pose.position.x = self.rest_x
        pose.pose.position.y = self.rest_y
        pose.pose.position.z = self.rest_z

        self.set_gripper_orientation(pose)

        return pose

    def pick_and_place(self, goal_handle):
        """
        Execute the complete pick-and-place routine.

        Sequence:
            1. Open gripper narrowly.
            2. Move above pickup location.
            3. Descend incrementally.
            4. Close gripper.
            5. Lift block.
            6. Move above placement location.
            7. Descend incrementally.
            8. Release block.
            9. Retreat safely to rest pose.

        """
        # Create hover poses
        pickup_hover = copy.deepcopy(goal_handle.request.pickup_pose)
        place_hover = copy.deepcopy(goal_handle.request.place_pose)

        pickup_hover.header.frame_id = "base"
        place_hover.header.frame_id = "base"

        pickup_hover.pose.position.z = self.hover_z
        place_hover.pose.position.z = self.hover_z

        self.set_gripper_orientation(pickup_hover)
        self.set_gripper_orientation(place_hover)

        # Open gripper before pickup
        self.publish_feedback(goal_handle, "Opening gripper")

        if not self.open_gripper_narrow():
            return False, "Failed to open gripper"

        # Move to pickup hover position
        self.publish_feedback(goal_handle, "Moving to pickup hover")

        if not self.move_to_pose(pickup_hover, "pickup hover"):
            return False, "Failed to move to pickup hover"

        # Descend toward block in increments, going all at once messes up 
        # the gripper orientation
        self.publish_feedback(goal_handle, "Descending to pickup")

        for i, z in enumerate(self.pick_descend_steps):
            p = copy.deepcopy(pickup_hover)
            p.pose.position.z = z

            if not self.move_to_pose(p, f"pickup descend step {i}"):
                return False, f"Failed during pickup descend step {i}"

        # Close gripper around block
        self.publish_feedback(goal_handle, "Closing gripper")

        if not self.close_gripper():
            return False, "Failed to close gripper"

        # Allow gripper time to fully close
        time.sleep(1.5)

        # Lift block
        self.publish_feedback(goal_handle, "Lifting block")

        if not self.move_to_pose(pickup_hover, "lift from pickup"):
            return False, "Failed to lift block"

        # Move above placement location
        self.publish_feedback(goal_handle, "Moving to place hover")

        if not self.move_to_pose(place_hover, "place hover"):
            return False, "Failed to move to place hover"

        # Descend toward placement location
        self.publish_feedback(goal_handle, "Descending to place")

        place_low = None

        for i, z in enumerate(self.place_descend_steps):
            p = copy.deepcopy(place_hover)
            p.pose.position.z = z

            place_low = copy.deepcopy(p)

            if not self.move_to_pose(p, f"place descend step {i}"):
                return False, f"Failed during place descend step {i}"

        # Release block
        self.publish_feedback(goal_handle, "Opening gripper at place location")

        if not self.open_gripper():
            return False, "Failed to open gripper at place location"

        time.sleep(0.5)


        # Retreat to rest pose before next block pickup.
        self.publish_feedback(goal_handle, "Moving to rest pose")

        if not self.move_to_rest(place_low):
            return False, "Failed to move to rest pose after placing"

        self.publish_feedback(goal_handle, "Pick and place complete")

        return True, "Pick and place complete"

    def move_to_rest(self, start_pose):
        """
        Retreat from the placement location to rest pose safely. By giving
        intermediate poses to get to, avoids moveit sending weird trajectories. 
        """
        rest_pose = self.make_rest_pose()

        sx = start_pose.pose.position.x
        sy = start_pose.pose.position.y
        sz = start_pose.pose.position.z

        rx = rest_pose.pose.position.x
        ry = rest_pose.pose.position.y
        rz = rest_pose.pose.position.z

        # Safe travel height
        safe_z = max(rz, self.hover_z, sz)

        steps = []

        # Lift vertically upward
        lift_steps = 4

        for i in range(1, lift_steps + 1):
            a = i / float(lift_steps)

            p = copy.deepcopy(start_pose)

            p.header.frame_id = "base"

            p.pose.position.x = sx
            p.pose.position.y = sy
            p.pose.position.z = sz + a * (safe_z - sz)

            self.set_gripper_orientation(p)

            steps.append(p)

        # Travel toward rest pose
        travel_steps = 6

        for i in range(1, travel_steps + 1):
            a = i / float(travel_steps)

            p = copy.deepcopy(rest_pose)

            p.pose.position.x = sx + a * (rx - sx)
            p.pose.position.y = sy + a * (ry - sy)
            p.pose.position.z = safe_z + a * (rz - safe_z)

            self.set_gripper_orientation(p)

            steps.append(p)

        # Execute retreat trajectory
        for i, p in enumerate(steps):
            if not self.move_to_pose(p, f"rest step {i + 1}/{len(steps)}"):
                return False

        return True

    def set_gripper_orientation(self, pose: PoseStamped):
        """
        Apply a fixed gripper orientation to a pose.
        """
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
        """
        Block until an asynchronous ROS future completes.
        """
        event = threading.Event()

        future.add_done_callback(lambda _: event.set())

        ok = event.wait(timeout=timeout_sec)

        if not ok:
            return None

        return future.result()

    def call_empty_service(self, client, name):
        """
        Call a std_srvs/Empty service safely (used for calling gripper services)
        """
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
        """
        Close the gripper fully.
        """
        return self.call_empty_service(
            self.gripper_close_client,
            "gripper close"
        )


    def open_gripper_narrow(self):
        """
        Open the gripper narrowly so we don't hit other blocks
        """
        return self.call_empty_service(
            self.gripper_open_narrow_client,
            "gripper open"
        )

    def move_to_pose(self, pose, label="pose"):
        """
        Send a MoveIt motion request to a target pose.
        """
        pose.header.stamp = self.get_clock().now().to_msg()

        self.get_logger().info(
            f"Moving to {label}: "
            f"x={pose.pose.position.x:.3f}, "
            f"y={pose.pose.position.y:.3f}, "
            f"z={pose.pose.position.z:.3f}"
        )

        # Wait for MoveIt action server
        if not self.move_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error("MoveIt /move_action server not available")
            return False

        # Build MoveIt goal
        goal = MoveGroup.Goal()

        goal.request.group_name = "ur_manipulator"

        goal.request.goal_constraints.append(
            self.pose_to_constraints(pose)
        )

        # Slow/safe motion scaling
        goal.request.max_velocity_scaling_factor = 0.05
        goal.request.max_acceleration_scaling_factor = 0.05

        # Send motion request
        send_future = self.move_client.send_goal_async(goal)

        goal_handle = self.wait_for_future(
            send_future,
            timeout_sec=10.0,
        )

        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error(f"Move goal rejected: {label}")
            return False

        # Wait for execution result
        result_future = goal_handle.get_result_async()

        result = self.wait_for_future(
            result_future,
            timeout_sec=60.0,
        )

        if result is None:
            self.get_logger().error(f"Move timed out: {label}")
            return False

        error_code = result.result.error_code.val

        # MoveIt SUCCESS == 1
        if error_code != 1:
            self.get_logger().error(
                f"Move failed: {label}, MoveIt error code {error_code}"
            )
            return False

        return True

    def pose_to_constraints(self, pose):
        """
        Convert a PoseStamped into MoveIt position/orientation constraints.
        """
        from moveit_msgs.msg import (
            Constraints,
            PositionConstraint,
            OrientationConstraint,
        )

        from shape_msgs.msg import SolidPrimitive

        constraints = Constraints()

        # Position constraint
        pc = PositionConstraint()

        pc.header = pose.header
        pc.link_name = "tool0"

        # Give MoveIt a small box to go to
        box = SolidPrimitive()

        box.type = SolidPrimitive.BOX
        box.dimensions = [0.01, 0.01, 0.01]

        pc.constraint_region.primitives.append(box)
        pc.constraint_region.primitive_poses.append(pose.pose)

        pc.weight = 1.0

        # Orientation constraint
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

        norm = math.sqrt(
            q.x*q.x +
            q.y*q.y +
            q.z*q.z +
            q.w*q.w
        )

        q.x /= norm
        q.y /= norm
        q.z /= norm
        q.w /= norm


def main(args=None):
    """
    ROS2 entry point.
    """
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