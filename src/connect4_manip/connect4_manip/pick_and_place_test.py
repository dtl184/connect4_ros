#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped
from connect4_msgs.action import PickAndPlace


class TestPickAndPlace(Node):
    def __init__(self, square):
        super().__init__("test_pick_and_place")

        self.square = square
        self.client = ActionClient(
            self,
            PickAndPlace,
            "/connect4/pick_and_place",
        )

        self.supply_poses = [
            self.make_pose(-0.173, -0.250, 0.100),
            self.make_pose(-0.111, -0.250, 0.100),
            self.make_pose(-0.030, -0.250, 0.100),
            self.make_pose(0.053, -0.250, 0.100),
        ]

        self.board_poses = {
            0: self.make_pose(-0.104, -0.481, 0.100),
            1: self.make_pose(-0.106, -0.428, 0.100),
            2: self.make_pose(-0.106, -0.366, 0.100),

            3: self.make_pose(-0.047, -0.489, 0.100),
            4: self.make_pose(-0.056, -0.435, 0.100),
            5: self.make_pose(-0.055, -0.372, 0.100),

            6: self.make_pose(-0.001, -0.491, 0.100),
            7: self.make_pose(0.009, -0.426, 0.100),
            8: self.make_pose(-0.005, -0.375, 0.100),
        }

        self.send_goal()

    def make_pose(self, x, y, z):
        pose = PoseStamped()
        pose.header.frame_id = "base"

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        pose.pose.orientation.x = 1.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 0.0

        return pose

    def send_goal(self):
        if self.square not in self.board_poses:
            self.get_logger().error("Square must be 0 through 8")
            rclpy.shutdown()
            return

        if not self.client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error("PickAndPlace server not available")
            rclpy.shutdown()
            return

        goal = PickAndPlace.Goal()
        goal.pickup_pose = self.supply_poses[0]
        goal.place_pose = self.board_poses[self.square]

        now = self.get_clock().now().to_msg()
        goal.pickup_pose.header.stamp = now
        goal.place_pose.header.stamp = now

        self.get_logger().info(f"Testing placement into square {self.square}")
        future = self.client.send_goal_async(goal)
        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error("Goal rejected")
            rclpy.shutdown()
            return

        self.get_logger().info("Goal accepted")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: success={result.success}, message={result.message}")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    square = 4
    if len(sys.argv) >= 2:
        square = int(sys.argv[1])

    node = TestPickAndPlace(square)
    rclpy.spin(node)


if __name__ == "__main__":
    main()