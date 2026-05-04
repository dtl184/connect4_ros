#!/usr/bin/env python3

import math
from typing import Optional, Tuple, List

import cv2
import numpy as np
import rclpy
from geometry_msgs.msg import Pose, PoseArray, PoseStamped
from pupil_apriltags import Detector
from connect4_msgs.msg import DetectedBlock, DetectedBlockArray
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image



HARDCODED_SRC_POINTS = np.array([
    [162.3, 64.6],
    [455.9, 72.6],
    [558.2, 459.4],
    [24.7, 441.8],
], dtype=np.float32)


class BlockPoseDetectorNode(Node):
    def __init__(self) -> None:
        super().__init__("block_pose_detector_node")

        self.declare_parameter("image_topic", "/image_raw")
        self.declare_parameter("pose_topic", "/detected_block_pose")
        self.declare_parameter("plane_frame_id", "box_top")
        self.declare_parameter("show_debug", True)

        self.declare_parameter("plane_width_m", 0.2159)
        self.declare_parameter("plane_height_m", 0.2794)
        self.declare_parameter("warp_width_px", 600)
        self.declare_parameter("warp_height_px", 600)

        self.declare_parameter("publish_only_tags_inside_board", True)

        self.image_topic = str(self.get_parameter("image_topic").value)
        self.pose_topic = str(self.get_parameter("pose_topic").value)
        self.plane_frame_id = str(self.get_parameter("plane_frame_id").value)
        self.show_debug = bool(self.get_parameter("show_debug").value)

        self.publish_only_tags_inside_board = bool(
            self.get_parameter("publish_only_tags_inside_board").value
        )

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

        self.src_points = HARDCODED_SRC_POINTS.astype(np.float32)

        if np.allclose(self.src_points, 0.0):
            self.get_logger().error(
                "HARDCODED_SRC_POINTS are still all zeros. "
                "Replace them with the points from your corner script."
            )

        self.H_img_to_warp = cv2.getPerspectiveTransform(
            self.src_points,
            self.dst_points_px,
        )

        self.H_warp_to_img = np.linalg.inv(self.H_img_to_warp)

        self.tag_detector = Detector(
            families="tag36h11",
            nthreads=1,
            quad_decimate=1.0,
            quad_sigma=0.0,
            refine_edges=1,
            decode_sharpening=0.25,
            debug=0,
        )

        self.image_sub = self.create_subscription(
            Image,
            self.image_topic,
            self.image_callback,
            qos_profile_sensor_data,
        )

        self.pose_pub = self.create_publisher(
            PoseStamped,
            self.pose_topic,
            10,
        )

        self.poses_pub = self.create_publisher(
            PoseArray,
            "/connect4/detected_block_pose_array",
            10,
        )

        self.detected_blocks_pub = self.create_publisher(
            DetectedBlockArray,
            "/connect4/detected_block_poses",
            10,
        )

        self.get_logger().info(f"Subscribed to image topic: {self.image_topic}")
        self.get_logger().info(f"Publishing single block pose to: {self.pose_topic}")
        self.get_logger().info(
            "Publishing debug PoseArray to: /connect4/detected_block_pose_array"
        )
        self.get_logger().info(
            "Publishing DetectedBlockArray to: /connect4/detected_block_poses"
        )
        self.get_logger().info("Using hardcoded board source points.")
        self.get_logger().info("Using pupil_apriltags family: tag36h11")

    def image_callback(self, msg: Image) -> None:
        frame = self.ros_image_to_bgr(msg)
        if frame is None:
            return

        raw_debug = frame.copy()
        self.draw_source_polygon(raw_debug)

        warped = cv2.warpPerspective(
            frame,
            self.H_img_to_warp,
            (self.warp_width_px, self.warp_height_px),
        )

        warp_debug = warped.copy()
        detections = self.detect_apriltags_in_warped(warped)

        pose_array = PoseArray()
        pose_array.header = msg.header
        pose_array.header.frame_id = self.plane_frame_id

        detected_array = DetectedBlockArray()
        valid_pose_infos = []

        for tag_id, center_warp, corners_warp, yaw_deg in detections:
            x_plane, y_plane = self.warp_px_to_plane_xy(center_warp)
            if x_plane is None or y_plane is None:
                continue

            pose = self.make_pose(x_plane, y_plane, yaw_deg)

            pose_array.poses.append(pose)

            block_msg = DetectedBlock()
            block_msg.id = int(tag_id)
            block_msg.pose = pose
            detected_array.blocks.append(block_msg)

            valid_pose_infos.append((tag_id, x_plane, y_plane, yaw_deg, center_warp))

            center_raw = self.warp_px_to_raw_px(center_warp)

            cv2.polylines(
                warp_debug,
                [corners_warp.astype(np.int32).reshape(-1, 1, 2)],
                True,
                (0, 255, 0),
                2,
            )
            cv2.circle(warp_debug, center_warp, 6, (0, 0, 255), -1)
            cv2.putText(
                warp_debug,
                f"id={tag_id} x={x_plane:.3f} y={y_plane:.3f}",
                (center_warp[0] + 8, center_warp[1] - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2,
                cv2.LINE_AA,
            )

            if center_raw is not None:
                cv2.circle(raw_debug, center_raw, 7, (0, 0, 255), -1)
                cv2.putText(
                    raw_debug,
                    f"tag {tag_id}",
                    (center_raw[0] + 10, center_raw[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

        self.poses_pub.publish(pose_array)
        self.detected_blocks_pub.publish(detected_array)

        if valid_pose_infos:
            tag_id, x_plane, y_plane, yaw_deg, _ = sorted(
                valid_pose_infos,
                key=lambda item: item[2],
            )[0]

            self.publish_single_block_pose(msg, x_plane, y_plane, yaw_deg)

            self.get_logger().info(
                f"Published {len(detected_array.blocks)} DetectedBlock messages",
                throttle_duration_sec=1.0,
            )
        else:
            self.get_logger().warn(
                "No AprilTags detected inside hardcoded board area",
                throttle_duration_sec=2.0,
            )

        if self.show_debug:
            cv2.putText(
                warp_debug,
                f"num_blocks={len(detected_array.blocks)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

            cv2.putText(
                warp_debug,
                "corners: hardcoded",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow("block_pose_raw", raw_debug)
            cv2.imshow("block_pose_warped", warp_debug)
            cv2.waitKey(1)

    def detect_apriltags_in_warped(
        self,
        warped_bgr: np.ndarray,
    ) -> List[Tuple[int, Tuple[int, int], np.ndarray, float]]:
        gray = cv2.cvtColor(warped_bgr, cv2.COLOR_BGR2GRAY)
        gray = np.ascontiguousarray(gray)

        tags = self.tag_detector.detect(gray)
        detections = []

        for tag in tags:
            tag_id = int(tag.tag_id)

            cx = int(tag.center[0])
            cy = int(tag.center[1])

            if self.publish_only_tags_inside_board:
                if cx < 0 or cx >= self.warp_width_px:
                    continue
                if cy < 0 or cy >= self.warp_height_px:
                    continue

            pts = np.array(tag.corners, dtype=np.float32)

            dx = float(pts[1, 0] - pts[0, 0])
            dy = float(pts[1, 1] - pts[0, 1])
            yaw_deg = math.degrees(math.atan2(dy, dx))

            detections.append((tag_id, (cx, cy), pts, yaw_deg))

        detections.sort(key=lambda d: d[0])
        return detections

    def publish_single_block_pose(
        self,
        img_msg: Image,
        x_plane: float,
        y_plane: float,
        angle_deg: float,
    ) -> None:
        pose_msg = self.make_pose_stamped_msg(img_msg, x_plane, y_plane, angle_deg)
        self.pose_pub.publish(pose_msg)

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

    def draw_source_polygon(self, frame: np.ndarray) -> None:
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

    def warp_px_to_plane_xy(
        self,
        warp_px: Tuple[int, int],
    ) -> Tuple[Optional[float], Optional[float]]:
        x_px, y_px = warp_px

        if self.warp_width_px <= 1 or self.warp_height_px <= 1:
            return None, None

        x_plane = (float(x_px) / float(self.warp_width_px - 1)) * self.plane_width_m
        y_plane = (float(y_px) / float(self.warp_height_px - 1)) * self.plane_height_m

        return x_plane, y_plane

    def warp_px_to_raw_px(
        self,
        warp_px: Tuple[int, int],
    ) -> Optional[Tuple[int, int]]:
        p = np.array([warp_px[0], warp_px[1], 1.0], dtype=np.float32)
        q = self.H_warp_to_img @ p

        if abs(q[2]) < 1e-6:
            return None

        q /= q[2]

        return int(q[0]), int(q[1])

    def make_pose(
        self,
        x: float,
        y: float,
        yaw_deg: float,
    ) -> Pose:
        pose = Pose()

        pose.position.x = x
        pose.position.y = y
        pose.position.z = 0.0

        yaw_rad = math.radians(yaw_deg)
        pose.orientation.x = 0.0
        pose.orientation.y = 0.0
        pose.orientation.z = math.sin(yaw_rad / 2.0)
        pose.orientation.w = math.cos(yaw_rad / 2.0)

        return pose

    def make_pose_stamped_msg(
        self,
        img_msg: Image,
        x: float,
        y: float,
        yaw_deg: float,
    ) -> PoseStamped:
        pose_msg = PoseStamped()
        pose_msg.header = img_msg.header
        pose_msg.header.frame_id = self.plane_frame_id
        pose_msg.pose = self.make_pose(x, y, yaw_deg)
        return pose_msg


def main(args=None) -> None:
    rclpy.init(args=args)
    node = BlockPoseDetectorNode()

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