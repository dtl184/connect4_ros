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
import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from connect4_msgs.action import TurtleDeliver


<<<<<<< HEAD
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
=======
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
>>>>>>> 3c4320a35d110b0c840f03d63b6ac0b503829f05
        goal = NavigateToPose.Goal()

        goal.pose = PoseStamped()

        goal.pose.header.frame_id = "map"

<<<<<<< HEAD
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
=======
        goal.pose.pose.position.x = float(x)
        goal.pose.pose.position.y = float(y)
        goal.pose.pose.position.z = 0.0

        qx, qy, qz, qw = yaw_to_quaternion(yaw)
        goal.pose.pose.orientation.x = qx
        goal.pose.pose.orientation.y = qy
        goal.pose.pose.orientation.z = qz
        goal.pose.pose.orientation.w = qw

        return goal
>>>>>>> 3c4320a35d110b0c840f03d63b6ac0b503829f05

    def send_nav_goal_and_wait(self, x, y, yaw, status_text, goal_handle):
        feedback = TurtleDeliver.Feedback()
        feedback.status = status_text
        goal_handle.publish_feedback(feedback)

<<<<<<< HEAD
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
=======
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
>>>>>>> 3c4320a35d110b0c840f03d63b6ac0b503829f05


def main(args=None):
    rclpy.init(args=args)

<<<<<<< HEAD
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
=======
    node = TurtleDeliverServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()
>>>>>>> 3c4320a35d110b0c840f03d63b6ac0b503829f05


if __name__ == "__main__":
    main()