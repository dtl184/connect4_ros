#!/usr/bin/env python3

import time
from typing import List, Optional

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Pose, PoseStamped

from connect4_msgs.action import ResetBoard, PickAndDrop
from connect4_msgs.msg import DetectedBlockArray, DetectedBlock


class ResetBoardActionServer(Node):
    def __init__(self):
        super().__init__("reset_board_action_server")

        self.callback_group = ReentrantCallbackGroup()

        self.latest_blocks: Optional[List[DetectedBlock]] = None
        self.latest_blocks_time: Optional[float] = None

        self.block_sub = self.create_subscription(
            DetectedBlockArray,
            "/connect4/detected_block_poses",
            self.blocks_callback,
            10,
            callback_group=self.callback_group,
        )

        # Existing PickAndDrop server expects one selected block here.
        self.selected_block_pub = self.create_publisher(
            PoseStamped,
            "/detected_block_pose",
            10,
        )

        self.pick_client = ActionClient(
            self,
            PickAndDrop,
            "/connect4/pick_and_drop",
            callback_group=self.callback_group,
        )

        self.reset_server = ActionServer(
            self,
            ResetBoard,
            "/connect4/reset_board",
            self.execute_callback,
            callback_group=self.callback_group,
        )

        self.get_logger().info("ResetBoard action server ready")
        self.get_logger().info("Listening for blocks on /connect4/detected_block_poses")
        self.get_logger().info("Publishing selected block to /detected_block_pose")
        self.get_logger().info("Calling PickAndDrop action on /connect4/pick_and_drop")

    def blocks_callback(self, msg: DetectedBlockArray):
        self.latest_blocks = list(msg.blocks)
        self.latest_blocks_time = time.time()

        # self.get_logger().info(
        #     f"Reset server sees {len(self.latest_blocks)} detected blocks"
        # )

    def make_result(self, success: bool, message: str):
        result = ResetBoard.Result()

        # These fields exist in your action based on your terminal output.
        if hasattr(result, "success"):
            result.success = success

        if hasattr(result, "message"):
            result.message = message

        return result

    def get_current_blocks(self, timeout_sec: float = 5.0) -> List[DetectedBlock]:
        start = time.time()

        while rclpy.ok():
            if self.latest_blocks is not None:
                # Return a copy so it doesn't change while resetting.
                return list(self.latest_blocks)

            if time.time() - start > timeout_sec:
                return []

            time.sleep(0.05)

        return []

    def choose_next_block(self, blocks: List[DetectedBlock]) -> DetectedBlock:
        """
        Choose which block to remove next.

        For now: remove the block with smallest y first.
        Change this later if you want a different cleanup order.
        """
        return sorted(blocks, key=lambda b: b.pose.position.y)[0]

    def publish_selected_block(self, pose: Pose):
        msg = PoseStamped()
        msg.header.frame_id = "box_top"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose = pose

        self.selected_block_pub.publish(msg)

        self.get_logger().info(
            f"Published selected block pose: "
            f"x={pose.position.x:.4f}, "
            f"y={pose.position.y:.4f}, "
            f"z={pose.position.z:.4f}"
        )

    async def call_pick_and_drop(self) -> bool:
        if not self.pick_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error("PickAndDrop action server not available")
            return False

        goal = PickAndDrop.Goal()

        send_future = self.pick_client.send_goal_async(goal)
        goal_handle = await send_future

        if not goal_handle.accepted:
            self.get_logger().error("PickAndDrop goal rejected")
            return False

        self.get_logger().info("PickAndDrop goal accepted")

        result_future = goal_handle.get_result_async()
        result = await result_future

        self.get_logger().info("PickAndDrop action finished")
        return result is not None and result.result.success

    async def execute_callback(self, goal_handle):
        self.get_logger().info("ResetBoard goal received")

        max_attempts = 20
        picked_count = 0

        for attempt in range(max_attempts):
            blocks = self.get_current_blocks(timeout_sec=3.0)

            if len(blocks) == 0:
                self.get_logger().warn("No blocks detected. Cannot reset.")
                goal_handle.succeed()
                return self.make_result(False, "No blocks detected")

            self.get_logger().info(f"Reset attempt {attempt + 1}: {len(blocks)} blocks visible")

            target_block = self.choose_next_block(blocks)
            target_pose = target_block.pose

            self.get_logger().info(
                f"Selected tag {target_block.id}: "
                f"x={target_pose.position.x:.4f}, "
                f"y={target_pose.position.y:.4f}, "
                f"z={target_pose.position.z:.4f}"
            )

            self.publish_selected_block(target_pose)

            # Give PickAndDrop time to receive /detected_block_pose.
            time.sleep(0.3)

            ok = await self.call_pick_and_drop()

            if not ok:
                self.get_logger().error("PickAndDrop failed during reset")
                goal_handle.abort()
                return self.make_result(False, "PickAndDrop failed")

            picked_count += 1

            # Clear old blocks so we wait for fresh perception after moving.
            self.latest_blocks = None
            self.latest_blocks_time = None

            time.sleep(1.0)

        self.get_logger().warn(
            f"Stopped after max_attempts={max_attempts}. Picked {picked_count} blocks."
        )

        goal_handle.succeed()
        return self.make_result(
            True,
            f"Reset stopped after max attempts. Picked {picked_count} blocks.",
        )


def main(args=None):
    rclpy.init(args=args)

    node = ResetBoardActionServer()

    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()