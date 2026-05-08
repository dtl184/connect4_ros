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


# Starting / home pose in the map frame.
# Tune these to wherever the TurtleBot starts in RViz.
HOME_X = 0.0
HOME_Y = 0.0
HOME_YAW = 0.0


def yaw_to_quaternion(yaw):
    qz = math.sin(yaw / 2.0)
    qw = math.cos(yaw / 2.0)
    return 0.0, 0.0, qz, qw


def normalize_yaw(yaw):
    return math.atan2(math.sin(yaw), math.cos(yaw))


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

    def send_nav_goal_and_wait(self, x, y, yaw, status_text, goal_handle):
        feedback = TurtleDeliver.Feedback()
        feedback.status = status_text
        goal_handle.publish_feedback(feedback)

        nav_goal = self.make_nav_goal(x, y, yaw)

        send_future = self.nav_client.send_goal_async(nav_goal)
        rclpy.spin_until_future_complete(self, send_future)

        nav_goal_handle = send_future.result()

        if nav_goal_handle is None or not nav_goal_handle.accepted:
            return False, "Nav2 rejected goal."

        result_future = nav_goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        nav_result = result_future.result()

        if nav_result is None:
            return False, "No result returned from Nav2."

        return True, "Nav2 goal completed."

    def execute_callback(self, goal_handle):
        x = goal_handle.request.x
        y = goal_handle.request.y
        yaw = goal_handle.request.yaw

        result = TurtleDeliver.Result()
        feedback = TurtleDeliver.Feedback()

        feedback.status = "Waiting for Nav2 /navigate_to_pose action server..."
        goal_handle.publish_feedback(feedback)

        self.get_logger().info("Waiting for Nav2...")
        self.nav_client.wait_for_server()

        ok, msg = self.send_nav_goal_and_wait(
            x,
            y,
            yaw,
            f"Driving to delivery location: x={x:.2f}, y={y:.2f}, yaw={yaw:.2f}",
            goal_handle,
        )

        if not ok:
            result.success = False
            result.message = f"Delivery failed: {msg}"
            goal_handle.abort()
            return result

        feedback.status = "Arrived. Waiting briefly..."
        goal_handle.publish_feedback(feedback)
        time.sleep(2.0)

        turnaround_yaw = normalize_yaw(yaw + math.pi)

        ok, msg = self.send_nav_goal_and_wait(
            x,
            y,
            turnaround_yaw,
            "Turning around...",
            goal_handle,
        )

        if not ok:
            result.success = False
            result.message = f"Turnaround failed: {msg}"
            goal_handle.abort()
            return result

        feedback.status = "Waiting briefly before returning home..."
        goal_handle.publish_feedback(feedback)
        time.sleep(1.0)

        ok, msg = self.send_nav_goal_and_wait(
            HOME_X,
            HOME_Y,
            HOME_YAW,
            f"Returning home: x={HOME_X:.2f}, y={HOME_Y:.2f}, yaw={HOME_YAW:.2f}",
            goal_handle,
        )

        if not ok:
            result.success = False
            result.message = f"Return home failed: {msg}"
            goal_handle.abort()
            return result

        result.success = True
        result.message = "Delivery complete and robot returned home."
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