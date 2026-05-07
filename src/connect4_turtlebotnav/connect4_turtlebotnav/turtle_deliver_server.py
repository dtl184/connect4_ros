#!/usr/bin/env python3

import time
import math

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from connect4_msgs.action import TurtleDeliver


class TurtleDeliverServer(Node):
    def __init__(self):
        super().__init__("turtle_deliver_server")

        self.cb_group = ReentrantCallbackGroup()

        self.server = ActionServer(
            self,
            TurtleDeliver,
            "/connect4/turtle_deliver",
            self.execute_callback,
            callback_group=self.cb_group,
        )

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            "/navigate_to_pose",
            callback_group=self.cb_group,
        )

        # HARD CODED LOCATIONS.
        # Replace these with your actual map-frame poses.
        self.home_pose = self.make_pose(
            x=0.0,
            y=0.0,
            yaw=0.0,
        )

        self.deliver_pose = self.make_pose(
            x=1.5,
            y=0.0,
            yaw=math.pi,
        )

        self.wait_seconds = 3.0

        self.get_logger().info("Turtle deliver action server ready.")

    def make_pose(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = "map"

        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.position.z = 0.0

        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw

        return pose

    async def execute_callback(self, goal_handle):
        feedback = TurtleDeliver.Feedback()

        self.get_logger().info("Received turtle delivery request.")

        feedback.status = "Waiting for Nav2 action server..."
        goal_handle.publish_feedback(feedback)

        if not self.nav_client.wait_for_server(timeout_sec=10.0):
            goal_handle.abort()
            result = TurtleDeliver.Result()
            result.success = False
            result.message = "Nav2 /navigate_to_pose action server not available."
            return result

        feedback.status = "Going to delivery location..."
        goal_handle.publish_feedback(feedback)

        ok = await self.navigate_to(self.deliver_pose)

        if not ok:
            goal_handle.abort()
            result = TurtleDeliver.Result()
            result.success = False
            result.message = "Failed to reach delivery location."
            return result

        feedback.status = "Waiting at delivery location..."
        goal_handle.publish_feedback(feedback)
        time.sleep(self.wait_seconds)

        feedback.status = "Returning home..."
        goal_handle.publish_feedback(feedback)

        ok = await self.navigate_to(self.home_pose)

        if not ok:
            goal_handle.abort()
            result = TurtleDeliver.Result()
            result.success = False
            result.message = "Failed to return home."
            return result

        goal_handle.succeed()

        result = TurtleDeliver.Result()
        result.success = True
        result.message = "Delivery complete."
        return result

    async def navigate_to(self, pose_stamped):
        pose_stamped.header.stamp = self.get_clock().now().to_msg()

        goal = NavigateToPose.Goal()
        goal.pose = pose_stamped

        send_goal_future = self.nav_client.send_goal_async(goal)
        nav_goal_handle = await send_goal_future

        if not nav_goal_handle.accepted:
            self.get_logger().error("Nav2 rejected goal.")
            return False

        result_future = nav_goal_handle.get_result_async()
        result = await result_future

        status = result.status

        # 4 means STATUS_SUCCEEDED in action_msgs/msg/GoalStatus
        if status == 4:
            self.get_logger().info("Navigation goal succeeded.")
            return True

        self.get_logger().error(f"Navigation goal failed with status {status}.")
        return False


def main(args=None):
    rclpy.init(args=args)

    node = TurtleDeliverServer()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()