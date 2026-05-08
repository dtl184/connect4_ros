#!/usr/bin/env python3

"""
HTTP-to-ROS2 TurtleBot delivery bridge

This node exposes a simple Flask HTTP server that triggers
a TurtleBot navigation goal through Nav2.

ROS Interfaces
--------------

ACTION CLIENT:
    /navigate_to_pose
        Type: nav2_msgs/action/NavigateToPose
"""

import threading
import time

from flask import Flask, jsonify

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped


# Flask web server
app = Flask(__name__)

# Global ROS node reference used by Flask routes
ros_node = None


class TurtleDeliverNode(Node):
    """
    ROS2 node that sends TurtleBot navigation goals through Nav2.
    """

    def __init__(self):
        super().__init__("turtle_deliver_http_server")

        # Nav2 action client
        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            "/navigate_to_pose"
        )

    def send_delivery_goal(self):
        """
        Send a navigation goal to the TurtleBot.
        """

        self.get_logger().info(
            "Waiting for Nav2 action server..."
        )

        # Wait for Nav2 to become available
        self.nav_client.wait_for_server()

        # Create navigation goal
        goal = NavigateToPose.Goal()

        goal.pose = PoseStamped()

        goal.pose.header.frame_id = "map"

        goal.pose.header.stamp = (
            self.get_clock().now().to_msg()
        )

        # Target position
        goal.pose.pose.position.x = 0.3
        goal.pose.pose.position.y = 0.0
        goal.pose.pose.position.z = 0.0

        # Face forward
        goal.pose.pose.orientation.x = 0.0
        goal.pose.pose.orientation.y = 0.0
        goal.pose.pose.orientation.z = 0.0
        goal.pose.pose.orientation.w = 1.0

        self.get_logger().info(
            "Sending TurtleBot delivery goal..."
        )

        future = self.nav_client.send_goal_async(goal)

        def goal_response_callback(future):
            """
            Handle Nav2 goal response.
            """
            goal_handle = future.result()

            if not goal_handle.accepted:

                self.get_logger().error(
                    "Goal rejected"
                )

                return

            self.get_logger().info(
                "Goal accepted"
            )

            # Wait for navigation completion
            result_future = goal_handle.get_result_async()

            result_future.add_done_callback(
                result_callback
            )

        def result_callback(future):
            """
            Handle navigation completion.
            """
            self.get_logger().info(
                "Delivery complete"
            )

        future.add_done_callback(
            goal_response_callback
        )



# Flask HTTP things
@app.route("/deliver", methods=["POST", "GET"])
def deliver():
    """
    HTTP endpoint that triggers TurtleBot delivery.
    """

    def run_goal():
        """
        Execute navigation goal in background thread.
        This prevents Flask from blocking while the robot moves.
        """
        ros_node.send_delivery_goal()

    threading.Thread(
        target=run_goal,
        daemon=True
    ).start()

    return jsonify({"status": "started"})


def main():
    global ros_node

    # Initialize ROS2
    rclpy.init()

    ros_node = TurtleDeliverNode()
    ros_thread = threading.Thread(
        target=rclpy.spin,
        args=(ros_node,),
        daemon=True
    )

    ros_thread.start()

    # Start Flask server
    app.run(
        host="0.0.0.0",
        port=5000
    )


if __name__ == "__main__":
    main()