#!/usr/bin/env python3

import socket
import time

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty


ROBOT_IP = "192.168.1.2"
PORT = 63352

# Robotiq position values:
# 0   = fully open
# 255 = fully closed
#
# Tune this.
# Larger value = gripper opens LESS.
# Smaller value = gripper opens MORE.
NARROW_OPEN_POS = 95


class RobotiqGripperService(Node):
    def __init__(self):
        super().__init__("robotiq_gripper_service")

        self.open_srv = self.create_service(
            Empty,
            "/connect4/gripper/open",
            self.handle_open
        )

        self.open_narrow_srv = self.create_service(
            Empty,
            "/connect4/gripper/open_narrow",
            self.handle_open_narrow
        )

        self.close_srv = self.create_service(
            Empty,
            "/connect4/gripper/close",
            self.handle_close
        )

        self.get_logger().info("Robotiq gripper service ready.")
        self.activate()

    def send(self, cmd: str):
        with socket.create_connection((ROBOT_IP, PORT), timeout=3) as s:
            s.sendall((cmd + "\n").encode())
            time.sleep(0.05)

    def activate(self):
        self.get_logger().info("Activating gripper...")
        self.send("SET ACT 0")
        time.sleep(0.5)
        self.send("SET ACT 1")
        self.send("SET GTO 1")
        self.send("SET SPE 255")
        self.send("SET FOR 150")
        time.sleep(2.0)

    def set_position(self, pos: int, label: str):
        pos = max(0, min(255, int(pos)))
        self.get_logger().info(f"{label}: SET POS {pos}")
        self.send(f"SET POS {pos}")
        self.send("SET GTO 1")
        time.sleep(1.0)

    def open(self):
        self.set_position(0, "Opening gripper fully")

    def open_narrow(self):
        self.set_position(NARROW_OPEN_POS, "Opening gripper narrowly")

    def close(self):
        self.set_position(255, "Closing gripper")

    def handle_open(self, request, response):
        self.open()
        return response

    def handle_open_narrow(self, request, response):
        self.open_narrow()
        return response

    def handle_close(self, request, response):
        self.close()
        return response


def main():
    rclpy.init()
    node = RobotiqGripperService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()