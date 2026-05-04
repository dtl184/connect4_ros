#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
import cv2


class CornerDetector(Node):
    def __init__(self):
        super().__init__("corner_detector")

        self.subscription = self.create_subscription(
            Image,
            "/image_raw",
            self.image_callback,
            10
        )

        self.get_logger().info("Green corner detector running...")

        # HSV range for green (tune if needed)
        self.lower_green = np.array([35, 25, 80])
        self.upper_green = np.array([100, 255, 255])

    def image_callback(self, msg):
        frame = self.ros_image_to_bgr(msg)
        if frame is None:
            return

        corners = self.detect_green_corners(frame)

        debug = frame.copy()

        if corners is not None:
            corners = self.order_corners(corners)

            labels = ["TL", "TR", "BR", "BL"]
            for (x, y), label in zip(corners, labels):
                x_i, y_i = int(x), int(y)
                cv2.circle(debug, (x_i, y_i), 8, (0, 0, 255), -1)
                cv2.putText(
                    debug,
                    label,
                    (x_i + 5, y_i - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

            flat = corners.flatten().tolist()
            formatted = ", ".join([f"{v:.1f}" for v in flat])

            print("\nCOPY THIS:")
            print("[", formatted, "]")

        cv2.imshow("green_corner_detection", debug)
        cv2.waitKey(1)

    def detect_green_corners(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, self.lower_green, self.upper_green)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        blobs = []
        for c in contours:
            area = cv2.contourArea(c)
            if area < 100:
                continue

            M = cv2.moments(c)
            if abs(M["m00"]) < 1e-6:
                continue

            cx = M["m10"] / M["m00"]
            cy = M["m01"] / M["m00"]

            blobs.append((cx, cy, area))

        if len(blobs) < 4:
            return None

        blobs = sorted(blobs, key=lambda b: b[2], reverse=True)[:4]
        pts = np.array([[b[0], b[1]] for b in blobs], dtype=np.float32)

        return pts

    def order_corners(self, pts):
        ordered = np.zeros((4, 2), dtype=np.float32)

        s = pts.sum(axis=1)
        diff = np.diff(pts, axis=1).reshape(-1)

        ordered[0] = pts[np.argmin(s)]      # TL
        ordered[2] = pts[np.argmax(s)]      # BR
        ordered[1] = pts[np.argmin(diff)]   # TR
        ordered[3] = pts[np.argmax(diff)]   # BL

        return ordered

    def ros_image_to_bgr(self, msg):
        if msg.encoding == "rgb8":
            img = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))
            return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        elif msg.encoding == "bgr8":
            return np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))

        else:
            self.get_logger().warn(f"Unsupported encoding: {msg.encoding}")
            return None


def main():
    rclpy.init()
    node = CornerDetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()