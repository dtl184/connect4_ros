#!/usr/bin/env python3

from typing import Optional
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image


class GreenCornerPrinter(Node):
    def __init__(self):
        super().__init__("green_corner_printer")

        self.declare_parameter("image_topic", "/image_raw")
        self.declare_parameter("show_debug", True)

        self.declare_parameter("green_h_min", 35)
        self.declare_parameter("green_s_min", 25)
        self.declare_parameter("green_v_min", 80)
        self.declare_parameter("green_h_max", 100)
        self.declare_parameter("green_s_max", 255)
        self.declare_parameter("green_v_max", 255)

        self.declare_parameter("min_corner_area_px", 100.0)

        self.image_topic = str(self.get_parameter("image_topic").value)
        self.show_debug = bool(self.get_parameter("show_debug").value)

        self.green_lower = np.array([
            int(self.get_parameter("green_h_min").value),
            int(self.get_parameter("green_s_min").value),
            int(self.get_parameter("green_v_min").value),
        ], dtype=np.uint8)

        self.green_upper = np.array([
            int(self.get_parameter("green_h_max").value),
            int(self.get_parameter("green_s_max").value),
            int(self.get_parameter("green_v_max").value),
        ], dtype=np.uint8)

        self.min_corner_area_px = float(
            self.get_parameter("min_corner_area_px").value
        )

        self.printed_once = False

        self.sub = self.create_subscription(
            Image,
            self.image_topic,
            self.image_callback,
            qos_profile_sensor_data,
        )

        self.get_logger().info(f"Listening on image topic: {self.image_topic}")
        self.get_logger().info("Looking for 4 green tape corners...")

    def image_callback(self, msg: Image):
        frame = self.ros_image_to_bgr(msg)
        if frame is None:
            return

        debug = frame.copy()
        mask = self.make_green_mask(frame)

        pts = self.detect_green_corners(frame)

        if pts is None:
            self.get_logger().warn(
                "Could not find exactly 4 usable green corner blobs yet...",
                throttle_duration_sec=1.0,
            )

            if self.show_debug:
                cv2.imshow("raw", debug)
                cv2.imshow("green_mask", mask)
                cv2.waitKey(1)

            return

        self.draw_points(debug, pts)

        if not self.printed_once:
            self.printed_once = True

            self.get_logger().info("")
            self.get_logger().info("FOUND GREEN BOARD CORNERS")
            self.get_logger().info("Order is: TL, TR, BR, BL")
            self.get_logger().info("")
            self.get_logger().info("Paste this into your block detector:")
            self.get_logger().info("")
            print()
            print("self.src_points = np.array([")
            for x, y in pts:
                print(f"    [{x:.1f}, {y:.1f}],")
            print("], dtype=np.float32)")
            print()

            self.get_logger().info("Press Ctrl+C after verifying the debug window.")

        if self.show_debug:
            cv2.imshow("raw_with_ordered_corners", debug)
            cv2.imshow("green_mask", mask)
            cv2.waitKey(1)

    def ros_image_to_bgr(self, msg: Image) -> Optional[np.ndarray]:
        if msg.encoding in ["yuv422_yuy2", "yuyv", "yuv422"]:
            yuv = np.frombuffer(msg.data, dtype=np.uint8).reshape(
                (msg.height, msg.width, 2)
            )
            return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_YUY2)

        if msg.encoding == "rgb8":
            rgb = np.frombuffer(msg.data, dtype=np.uint8).reshape(
                (msg.height, msg.width, 3)
            )
            return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        if msg.encoding == "bgr8":
            return np.frombuffer(msg.data, dtype=np.uint8).reshape(
                (msg.height, msg.width, 3)
            )

        self.get_logger().warn(
            f"Unsupported encoding: {msg.encoding}",
            throttle_duration_sec=2.0,
        )
        return None

    def make_green_mask(self, bgr: np.ndarray) -> np.ndarray:
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.green_lower, self.green_upper)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        return mask

    def detect_green_corners(self, frame: np.ndarray) -> Optional[np.ndarray]:
        mask = self.make_green_mask(frame)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        blobs = []

        for c in contours:
            area = cv2.contourArea(c)
            if area < self.min_corner_area_px:
                continue

            m = cv2.moments(c)
            if abs(m["m00"]) < 1e-6:
                continue

            cx = m["m10"] / m["m00"]
            cy = m["m01"] / m["m00"]
            blobs.append((cx, cy, area))

        if len(blobs) < 4:
            return None

        # Take the 4 largest green blobs. Remove green blocks from the board
        # when running this script so the tape corners are the biggest blobs.
        blobs = sorted(blobs, key=lambda b: b[2], reverse=True)[:4]

        pts = np.array([[b[0], b[1]] for b in blobs], dtype=np.float32)
        return self.order_corners(pts)

    def order_corners(self, pts: np.ndarray) -> np.ndarray:
        ordered = np.zeros((4, 2), dtype=np.float32)

        s = pts.sum(axis=1)
        diff = np.diff(pts, axis=1).reshape(-1)

        ordered[0] = pts[np.argmin(s)]     # top-left
        ordered[2] = pts[np.argmax(s)]     # bottom-right
        ordered[1] = pts[np.argmin(diff)]  # top-right
        ordered[3] = pts[np.argmax(diff)]  # bottom-left

        return ordered

    def draw_points(self, frame: np.ndarray, pts: np.ndarray):
        labels = ["TL", "TR", "BR", "BL"]

        poly = pts.astype(np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [poly], True, (0, 255, 255), 2)

        for (x, y), label in zip(pts, labels):
            x = int(x)
            y = int(y)

            cv2.circle(frame, (x, y), 8, (255, 0, 0), -1)
            cv2.putText(
                frame,
                label,
                (x + 8, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2,
                cv2.LINE_AA,
            )


def main(args=None):
    rclpy.init(args=args)
    node = GreenCornerPrinter()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.show_debug:
            cv2.destroyAllWindows()

        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()