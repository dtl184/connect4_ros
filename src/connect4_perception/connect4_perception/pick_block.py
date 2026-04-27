#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped


class PickOrangeBlockNode(Node):
    def __init__(self):
        super().__init__('pick_orange_block_node')

        # Vision calibration point
        self.x0_vision = 0.1112671945876683
        self.y0_vision = 0.08971713001810504



        self.X0_robot = -0.04708
        self.Y0_robot = -0.40794
        self.Z_hover = -0.32675

        self.RX = 0.03
        self.RY = -3.143
        self.RZ = 0.124
        self.sub = self.create_subscription(
            PoseStamped,
            '/detected_block_pose',
            self.block_pose_callback,
            10
        )

        self.get_logger().info('PickOrangeBlockNode started')

    def block_pose_callback(self, msg: PoseStamped):
        x = msg.pose.position.x
        y = msg.pose.position.y

        X_robot = self.X0_robot + (x - self.x0_vision)
        Y_robot = self.Y0_robot + (y - self.y0_vision)
        Z_robot = self.Z_hover

        X_robot += 0.005
        Y_robot += 0.0

        self.get_logger().info(
            f'Detected vision pose: x={x:.4f}, y={y:.4f} -> '
            f'Robot hover pose: X={X_robot:.4f}, Y={Y_robot:.4f}, '
            f'Z={Z_robot:.4f}, RX={self.RX:.3f}, RY={self.RY:.3f}, RZ={self.RZ:.3f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = PickOrangeBlockNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()