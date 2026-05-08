#!/usr/bin/env python3

import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from connect4_msgs.action import TurtleDeliver


def yaw_to_quaternion(yaw):
    qz = math.sin(yaw / 2.0)
    qw = math.cos(yaw / 2.0)
    return 0.0, 0.0, qz, qw


class TurtleDeliverServer(Node):
    def __init__(self):
        super().__init__("turtle_deliver_server")

        self.server = ActionServer(
            self,
            TurtleDeliver,
            "/connect4/turtle_deliver",
            self.execute_callback,
        )

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            "/navigate_to_pose",
        )

        self.get_logger().info("Turtle deliver action server ready.")

    def make_nav_goal(self, x, y, yaw):
        goal = NavigateToPose.Goal()
        goal.pose = PoseStamped()

        goal.pose.header.frame_id = "map"
        goal.pose.header.stamp = self.get_clock().now().to_msg()

        goal.pose.pose.position.x = float(x)
        goal.pose.pose.position.y = float(y)
        goal.pose.pose.position.z = 0.0

        qx, qy, qz, qw = yaw_to_quaternion(yaw)
        goal.pose.pose.orientation.x = qx
        goal.pose.pose.orientation.y = qy
        goal.pose.pose.orientation.z = qz
        goal.pose.pose.orientation.w = qw

        return goal

    def execute_callback(self, goal_handle):
        x = goal_handle.request.x
        y = goal_handle.request.y
        yaw = goal_handle.request.yaw

        feedback = TurtleDeliver.Feedback()
        feedback.status = "Waiting for Nav2 /navigate_to_pose action server..."
        goal_handle.publish_feedback(feedback)

        self.get_logger().info("Waiting for Nav2...")
        self.nav_client.wait_for_server()

        feedback.status = f"Sending delivery goal: x={x:.2f}, y={y:.2f}, yaw={yaw:.2f}"
        goal_handle.publish_feedback(feedback)

        nav_goal = self.make_nav_goal(x, y, yaw)

        send_future = self.nav_client.send_goal_async(nav_goal)
        rclpy.spin_until_future_complete(self, send_future)

        nav_goal_handle = send_future.result()

        result = TurtleDeliver.Result()

        if nav_goal_handle is None or not nav_goal_handle.accepted:
            result.success = False
            result.message = "Nav2 rejected the delivery goal."
            goal_handle.abort()
            return result

        feedback.status = "Nav2 goal accepted. Driving to delivery location..."
        goal_handle.publish_feedback(feedback)

        result_future = nav_goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        nav_result = result_future.result()

        if nav_result is None:
            result.success = False
            result.message = "No result returned from Nav2."
            goal_handle.abort()
            return result

        feedback.status = "Arrived. Waiting briefly..."
        goal_handle.publish_feedback(feedback)

        time.sleep(2.0)

        # Turn around in place by sending same x/y with yaw + pi.
        turnaround_yaw = yaw + math.pi
        turnaround_goal = self.make_nav_goal(x, y, turnaround_yaw)

        feedback.status = "Turning around..."
        goal_handle.publish_feedback(feedback)

        turn_future = self.nav_client.send_goal_async(turnaround_goal)
        rclpy.spin_until_future_complete(self, turn_future)

        turn_goal_handle = turn_future.result()

        if turn_goal_handle is not None and turn_goal_handle.accepted:
            turn_result_future = turn_goal_handle.get_result_async()
            rclpy.spin_until_future_complete(self, turn_result_future)

        result.success = True
        result.message = "Delivery complete."
        goal_handle.succeed()
        return result


def main(args=None):
    rclpy.init(args=args)

    node = TurtleDeliverServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()