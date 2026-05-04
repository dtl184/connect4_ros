#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
import time

from geometry_msgs.msg import PoseStamped
from moveit_msgs.action import MoveGroup


class MoveItPoseClient(Node):
    def __init__(self):
        super().__init__('moveit_pose_client')

        self.client = ActionClient(self, MoveGroup, '/move_action')

        self.script_pub = self.create_publisher(String, "/urscript_interface/script_command", 10)

    def send_goal(self):
        self.get_logger().info("Waiting for MoveIt action server...")
        self.client.wait_for_server()

        goal = MoveGroup.Goal()

        # ---- YOUR POSE ----
        pose = PoseStamped()
        pose.header.frame_id = "base"

        pose.pose.position.x = -0.07939464487979704
        pose.pose.position.y = -0.4872288619907205
        pose.pose.position.z = 0.08506966228172184

        pose.pose.position.x += 0.01
        pose.pose.position.y += 0.03

        # Quaternion from your RX,RY,RZ


        pose.pose.orientation.x = -0.012
        pose.pose.orientation.y = 1.000
        pose.pose.orientation.z = 0.021
        pose.pose.orientation.w = 0.014

        # ---- Constraints ----
        goal.request.group_name = "ur_manipulator"
        goal.request.goal_constraints.append(
            self.pose_to_constraints(pose)
        )

        goal.request.num_planning_attempts = 5
        goal.request.allowed_planning_time = 5.0
        goal.request.max_velocity_scaling_factor = 0.05
        goal.request.max_acceleration_scaling_factor = 0.05

        self.get_logger().info("Sending goal...")
        future = self.client.send_goal_async(goal)

        rclpy.spin_until_future_complete(self, future)

        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        self.get_logger().info("Done.")

    def pose_to_constraints(self, pose):
        from moveit_msgs.msg import Constraints, PositionConstraint, OrientationConstraint
        from shape_msgs.msg import SolidPrimitive

        constraints = Constraints()

        # Position constraint
        pc = PositionConstraint()
        pc.header = pose.header
        pc.link_name = "tool0"

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
        oc.absolute_x_axis_tolerance = 0.1
        oc.absolute_y_axis_tolerance = 0.1
        oc.absolute_z_axis_tolerance = 0.1
        oc.weight = 1.0

        constraints.position_constraints.append(pc)
        constraints.orientation_constraints.append(oc)

        return constraints




def main():
    rclpy.init()
    node = MoveItPoseClient()
    node.send_goal()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()