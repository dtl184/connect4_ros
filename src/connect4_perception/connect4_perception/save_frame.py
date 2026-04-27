#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np


class SaveFrame(Node):
    def __init__(self):
        super().__init__('save_frame')
        self.sub = self.create_subscription(Image, '/image_raw', self.cb, 10)

    def cb(self, msg):
        if msg.encoding == 'rgb8':
            arr = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)
            bgr = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
        elif msg.encoding == 'bgr8':
            bgr = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)
        else:
            self.get_logger().error(f'Unsupported encoding: {msg.encoding}')
            return

        cv2.imwrite('paper_frame.jpg', bgr)
        self.get_logger().info(f'Saved paper_frame.jpg at {msg.width}x{msg.height}')
        rclpy.shutdown()


rclpy.init()
node = SaveFrame()
rclpy.spin(node)