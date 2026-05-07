#!/usr/bin/env python3

import threading
import time

from flask import Flask, jsonify

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped


app = Flask(__name__)
ros_node = None


class TurtleDeliverNode(Node):
    def __init__(self):
        super().__init__("turtle_deliver_http_server")
        self.nav_client = ActionClient(self, NavigateToPose, "/navigate_to_pose")

    def send_delivery_goal(self):
        self.get_logger().info("Waiting for Nav2 action server...")
        self.nav_client.wait_for_server()

        goal = NavigateToPose.Goal()
        goal.pose = PoseStamped()

        goal.pose.header.frame_id = "map"
        goal.pose.header.stamp = self.get_clock().now().to_msg()

        # small forward motion
        goal.pose.pose.position.x = 0.3
        goal.pose.pose.position.y = 0.0
        goal.pose.pose.position.z = 0.0

        goal.pose.pose.orientation.x = 0.0
        goal.pose.pose.orientation.y = 0.0
        goal.pose.pose.orientation.z = 0.0
        goal.pose.pose.orientation.w = 1.0

        self.get_logger().info("Sending TurtleBot delivery goal...")

        future = self.nav_client.send_goal_async(goal)

        def goal_response_callback(future):
            goal_handle = future.result()

            if not goal_handle.accepted:
                self.get_logger().error("Goal rejected")
                return

            self.get_logger().info("Goal accepted")

            result_future = goal_handle.get_result_async()
            result_future.add_done_callback(result_callback)

        def result_callback(future):
            self.get_logger().info("Delivery complete")

        future.add_done_callback(goal_response_callback)

@app.route("/deliver", methods=["POST", "GET"])
def deliver():
    def run_goal():
        ros_node.send_delivery_goal()

    threading.Thread(target=run_goal, daemon=True).start()
    return jsonify({"status": "started"})


def main():
    global ros_node

    rclpy.init()
    ros_node = TurtleDeliverNode()

    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True)
    ros_thread.start()

    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()