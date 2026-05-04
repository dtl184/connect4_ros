#!/usr/bin/env python3

import math
from typing import Optional, Tuple

import cv2
import numpy as np
import rclpy
from geometry_msgs.msg import PoseStamped
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image


class OrangeBlockDetectorNode(Node):
    def __init__(self) -> None:
        super().__init__("orange_block_detector_node")

        self.declare_parameter("image_topic", "/image_raw")
        self.declare_parameter("pose_topic", "/detected_block_pose")
        self.declare_parameter("plane_frame_id", "box_top")
        self.declare_parameter("show_debug", True)

        # Green tape corner HSV threshold
        self.declare_parameter("green_h_min", 35)
        self.declare_parameter("green_s_min", 25)
        self.declare_parameter("green_v_min", 80)
        self.declare_parameter("green_h_max", 100)
        self.declare_parameter("green_s_max", 255)
        self.declare_parameter("green_v_max", 255)
        self.declare_parameter("min_corner_area_px", 100.0)

        # Orange block HSV threshold
        self.declare_parameter("orange_h_min", 20)
        self.declare_parameter("orange_s_min", 100)
        self.declare_parameter("orange_v_min", 100)
        self.declare_parameter("orange_h_max", 35)
        self.declare_parameter("orange_s_max", 255)
        self.declare_parameter("orange_v_max", 255)

        self.declare_parameter("min_contour_area_px", 200.0)
        self.declare_parameter("blur_kernel", 5)
        self.declare_parameter("morph_kernel", 5)

        # Paper / board size in meters
        self.declare_parameter("plane_width_m", 0.2159)
        self.declare_parameter("plane_height_m", 0.2794)

        self.declare_parameter("warp_width_px", 600)
        self.declare_parameter("warp_height_px", 600)

        self.image_topic = str(self.get_parameter("image_topic").value)
        self.pose_topic = str(self.get_parameter("pose_topic").value)
        self.plane_frame_id = str(self.get_parameter("plane_frame_id").value)
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

        self.orange_lower = np.array([
            int(self.get_parameter("orange_h_min").value),
            int(self.get_parameter("orange_s_min").value),
            int(self.get_parameter("orange_v_min").value),
        ], dtype=np.uint8)

        self.orange_upper = np.array([
            int(self.get_parameter("orange_h_max").value),
            int(self.get_parameter("orange_s_max").value),
            int(self.get_parameter("orange_v_max").value),
        ], dtype=np.uint8)

        self.min_corner_area_px = float(self.get_parameter("min_corner_area_px").value)
        self.min_contour_area_px = float(self.get_parameter("min_contour_area_px").value)
        self.blur_kernel = int(self.get_parameter("blur_kernel").value)
        self.morph_kernel = int(self.get_parameter("morph_kernel").value)

        self.plane_width_m = float(self.get_parameter("plane_width_m").value)
        self.plane_height_m = float(self.get_parameter("plane_height_m").value)

        self.warp_width_px = int(self.get_parameter("warp_width_px").value)
        self.warp_height_px = int(self.get_parameter("warp_height_px").value)

        self.dst_points_px = np.array([
            [0.0, 0.0],
            [float(self.warp_width_px - 1), 0.0],
            [float(self.warp_width_px - 1), float(self.warp_height_px - 1)],
            [0.0, float(self.warp_height_px - 1)],
        ], dtype=np.float32)

        self.dst_points_m = np.array([
            [0.0, 0.0],
            [self.plane_width_m, 0.0],
            [self.plane_width_m, self.plane_height_m],
            [0.0, self.plane_height_m],
        ], dtype=np.float32)

        self.src_points: Optional[np.ndarray] = None
        self.H_img_to_warp: Optional[np.ndarray] = None
        self.H_img_to_plane: Optional[np.ndarray] = None

        self.image_sub = self.create_subscription(
            Image,
            self.image_topic,
            self.image_callback,
            qos_profile_sensor_data,
        )

        self.pose_pub = self.create_publisher(PoseStamped, self.pose_topic, 10)

        self.get_logger().info(f"Subscribed to {self.image_topic}")
        self.get_logger().info(f"Publishing block pose to {self.pose_topic}")
        self.get_logger().info(f"Plane frame: {self.plane_frame_id}")
        self.get_logger().info(
            f"Plane size: {self.plane_width_m:.3f} m x {self.plane_height_m:.3f} m"
        )

    def image_callback(self, msg: Image) -> None:
        frame = self.ros_image_to_bgr(msg)
        if frame is None:
            return

        detected_corners = self.detect_green_corners(frame)
        if detected_corners is None:
            self.get_logger().warn("Could not detect 4 green tape corners")
            if self.show_debug:
                cv2.imshow("orange_block_raw", frame)
                cv2.waitKey(1)
            return

        self.update_homographies_from_corners(detected_corners)

        warped = cv2.warpPerspective(
            frame,
            self.H_img_to_warp,
            (self.warp_width_px, self.warp_height_px),
        )

        detection = self.detect_orange_block(warped)

        raw_debug = frame.copy()
        warp_debug = warped.copy()

        self.draw_source_polygon(raw_debug)

        if detection is not None:
            center_px, angle_deg, contour = detection

            cv2.drawContours(warp_debug, [contour], -1, (0, 255, 0), 2)
            cv2.circle(warp_debug, center_px, 6, (0, 0, 255), -1)
            cv2.putText(
                warp_debug,
                f"center=({center_px[0]}, {center_px[1]}) angle={angle_deg:.1f}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

            center_raw = self.warp_px_to_raw_px(center_px)
            if center_raw is not None:
                cv2.circle(raw_debug, center_raw, 7, (0, 0, 255), -1)
                cv2.putText(
                    raw_debug,
                    "block",
                    (center_raw[0] + 10, center_raw[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

            x_plane, y_plane = self.raw_px_to_plane_xy(center_raw)
            if x_plane is not None and y_plane is not None:
                pose_msg = self.make_pose_msg(msg, x_plane, y_plane, angle_deg)
                self.pose_pub.publish(pose_msg)

                cv2.putText(
                    warp_debug,
                    f"x={x_plane:.3f}m y={y_plane:.3f}m",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 0, 0),
                    2,
                    cv2.LINE_AA,
                )

        if self.show_debug:
            _, orange_mask = self.make_orange_mask(warped)
            green_mask = self.make_green_mask(frame)

            cv2.imshow("orange_block_raw", raw_debug)
            cv2.imshow("orange_block_warped", warp_debug)
            cv2.imshow("orange_block_mask", orange_mask)
            cv2.imshow("green_corner_mask", green_mask)
            cv2.waitKey(1)

    def ros_image_to_bgr(self, msg: Image) -> Optional[np.ndarray]:
        if msg.encoding in ["yuv422_yuy2", "yuyv", "yuv422"]:
            yuv = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 2))
            return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_YUY2)

        if msg.encoding == "rgb8":
            rgb = np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))
            return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        if msg.encoding == "bgr8":
            return np.frombuffer(msg.data, dtype=np.uint8).reshape((msg.height, msg.width, 3))

        self.get_logger().warn(f"Unsupported encoding: {msg.encoding}")
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

            moment = cv2.moments(c)
            if abs(moment["m00"]) < 1e-6:
                continue

            cx = moment["m10"] / moment["m00"]
            cy = moment["m01"] / moment["m00"]
            blobs.append((cx, cy, area))

        if len(blobs) < 4:
            return None

        blobs = sorted(blobs, key=lambda b: b[2], reverse=True)[:4]
        pts = np.array([[b[0], b[1]] for b in blobs], dtype=np.float32)

        return self.order_corners(pts)

    def order_corners(self, pts: np.ndarray) -> np.ndarray:
        ordered = np.zeros((4, 2), dtype=np.float32)

        s = pts.sum(axis=1)
        diff = np.diff(pts, axis=1).reshape(-1)

        ordered[0] = pts[np.argmin(s)]       # top-left
        ordered[2] = pts[np.argmax(s)]       # bottom-right
        ordered[1] = pts[np.argmin(diff)]    # top-right
        ordered[3] = pts[np.argmax(diff)]    # bottom-left

        return ordered

    def update_homographies_from_corners(self, src_points: np.ndarray) -> None:
        self.src_points = src_points.astype(np.float32)

        self.H_img_to_warp = cv2.getPerspectiveTransform(
            self.src_points,
            self.dst_points_px,
        )

        self.H_img_to_plane = cv2.getPerspectiveTransform(
            self.src_points,
            self.dst_points_m,
        )

    def make_orange_mask(self, bgr: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        blurred = bgr
        if self.blur_kernel > 1:
            k = self.ensure_odd(self.blur_kernel)
            blurred = cv2.GaussianBlur(bgr, (k, k), 0)

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.orange_lower, self.orange_upper)

        k = max(1, self.morph_kernel)
        kernel = np.ones((k, k), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        return hsv, mask

    def detect_orange_block(
        self,
        warped_bgr: np.ndarray,
    ) -> Optional[Tuple[Tuple[int, int], float, np.ndarray]]:
        _, mask = self.make_orange_mask(warped_bgr)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [c for c in contours if cv2.contourArea(c) >= self.min_contour_area_px]

        if not contours:
            return None

        contour = max(contours, key=cv2.contourArea)
        moment = cv2.moments(contour)

        if abs(moment["m00"]) < 1e-6:
            return None

        cx = int(moment["m10"] / moment["m00"])
        cy = int(moment["m01"] / moment["m00"])

        rect = cv2.minAreaRect(contour)
        angle_deg = float(rect[2])

        return (cx, cy), angle_deg, contour

    def draw_source_polygon(self, frame: np.ndarray) -> None:
        if self.src_points is None:
            return

        pts = self.src_points.astype(np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 255), 2)

        labels = ["TL", "TR", "BR", "BL"]
        for (x, y), label in zip(self.src_points.astype(np.int32), labels):
            cv2.circle(frame, (int(x), int(y)), 7, (255, 0, 0), -1)
            cv2.putText(
                frame,
                label,
                (int(x) + 6, int(y) - 6),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),
                2,
                cv2.LINE_AA,
            )

    def raw_px_to_plane_xy(
        self,
        raw_px: Optional[Tuple[int, int]],
    ) -> Tuple[Optional[float], Optional[float]]:
        if raw_px is None or self.H_img_to_plane is None:
            return None, None

        p = np.array([raw_px[0], raw_px[1], 1.0], dtype=np.float32)
        q = self.H_img_to_plane @ p

        if abs(q[2]) < 1e-6:
            return None, None

        q /= q[2]
        return float(q[0]), float(q[1])

    def warp_px_to_raw_px(self, warp_px: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if self.H_img_to_warp is None:
            return None

        h_inv = np.linalg.inv(self.H_img_to_warp)
        p = np.array([warp_px[0], warp_px[1], 1.0], dtype=np.float32)
        q = h_inv @ p

        if abs(q[2]) < 1e-6:
            return None

        q /= q[2]
        return int(q[0]), int(q[1])

    def make_pose_msg(self, img_msg: Image, x: float, y: float, yaw_deg: float) -> PoseStamped:
        pose = PoseStamped()
        pose.header = img_msg.header
        pose.header.frame_id = self.plane_frame_id

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0

        yaw_rad = math.radians(yaw_deg)
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = math.sin(yaw_rad / 2.0)
        pose.pose.orientation.w = math.cos(yaw_rad / 2.0)

        return pose

    @staticmethod
    def ensure_odd(value: int) -> int:
        return value if value % 2 == 1 else value + 1


def main(args=None) -> None:
    rclpy.init(args=args)
    node = OrangeBlockDetectorNode()

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