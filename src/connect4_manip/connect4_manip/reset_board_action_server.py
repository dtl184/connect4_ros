#!/usr/bin/env python3

"""
Reset-board action server

This node automatically clears blocks from the board by:
    1. Listening to detected block poses from perception.
    2. Selecting a target block to remove.
    3. Publishing the selected block pose.
    4. Calling the PickAndDrop action server to remove the block.
    5. Repeating until no blocks remain or a maximum attempt count is reached.

ROS Interfaces
------------
SUBSCRIBES:
    /connect4/detected_block_poses
        Type: connect4_msgs/msg/DetectedBlockArray

ACTION CLIENT:
    /connect4/pick_and_drop
        Type: connect4_msgs/action/PickAndDrop

ACTION SERVER:
    /connect4/reset_board
        Type: connect4_msgs/action/ResetBoard
"""

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

        # Subscribe to detected blocks from perception.
        self.block_sub = self.create_subscription(
            DetectedBlockArray,
            "/connect4/detected_block_poses",
            self.blocks_callback,
            10,
            callback_group=self.callback_group,
        )

        self.selected_block_pub = self.create_publisher(
            PoseStamped,
            "/detected_block_pose",
            10,
        )

        # Action client for PickAndDrop manipulation.
        self.pick_client = ActionClient(
            self,
            PickAndDrop,
            "/connect4/pick_and_drop",
            callback_group=self.callback_group,
        )

        # ResetBoard action server.
        self.reset_server = ActionServer(
            self,
            ResetBoard,
            "/connect4/reset_board",
            self.execute_callback,
            callback_group=self.callback_group,
        )

        self.get_logger().info("ResetBoard action server ready")

        self.get_logger().info(
            "Listening for blocks on /connect4/detected_block_poses"
        )

        self.get_logger().info(
            "Publishing selected block to /detected_block_pose"
        )

        self.get_logger().info(
            "Calling PickAndDrop action on /connect4/pick_and_drop"
        )

    def blocks_callback(self, msg: DetectedBlockArray):

        self.latest_blocks = list(msg.blocks)

        self.latest_blocks_time = time.time()

    def make_result(self, success: bool, message: str):
        """
        Construct a ResetBoard action result.
        """
        result = ResetBoard.Result()


        if hasattr(result, "success"):
            result.success = success

        if hasattr(result, "message"):
            result.message = message

        return result

    def get_current_blocks(
        self,
        timeout_sec: float = 5.0
    ) -> List[DetectedBlock]:
        """
        Wait for and retrieve the latest detected blocks.
        """
        start = time.time()

        while rclpy.ok():

            # Return a copy to avoid mutation during reset.
            if self.latest_blocks is not None:
                return list(self.latest_blocks)

            if time.time() - start > timeout_sec:
                return []

            time.sleep(0.05)

        return []

    def choose_next_block(
        self,
        blocks: List[DetectedBlock]
    ) -> DetectedBlock:
        """
        Choose which block to remove next.

        Current strategy: remove the block with the smallest y coordinate first.
        This effectively removes the "top-most" block first.
        """
        return sorted(
            blocks,
            key=lambda b: b.pose.position.y
        )[0]

    def publish_selected_block(self, pose: Pose):
        """
        Publish the currently selected target block pose.
        This topic is consumed by the PickAndDrop server.
        """
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
        """
        Call the PickAndDrop action server.
        """
        # Wait for action server
        if not self.pick_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error(
                "PickAndDrop action server not available"
            )

            return False

        goal = PickAndDrop.Goal()

        # Send action goal
        send_future = self.pick_client.send_goal_async(goal)

        goal_handle = await send_future

        if not goal_handle.accepted:
            self.get_logger().error("PickAndDrop goal rejected")
            return False

        self.get_logger().info("PickAndDrop goal accepted")

        # Wait for completion
        result_future = goal_handle.get_result_async()

        result = await result_future

        self.get_logger().info("PickAndDrop action finished")

        return result is not None and result.result.success

    async def execute_callback(self, goal_handle):
        """
        Main ResetBoard action callback.
        """
        self.get_logger().info("ResetBoard goal received")

        # Safety limit to avoid infinite loops
        max_attempts = 20

        picked_count = 0

        for attempt in range(max_attempts):

            # Get latest perception state
            blocks = self.get_current_blocks(timeout_sec=3.0)

            # If no visible blocks
            if len(blocks) == 0:
                self.get_logger().warn(
                    "No blocks detected. Cannot reset."
                )

                goal_handle.succeed()

                return self.make_result(
                    False,
                    "No blocks detected"
                )

            self.get_logger().info(
                f"Reset attempt {attempt + 1}: "
                f"{len(blocks)} blocks visible"
            )

            # Choose target block
            target_block = self.choose_next_block(blocks)

            target_pose = target_block.pose

            self.get_logger().info(
                f"Selected tag {target_block.id}: "
                f"x={target_pose.position.x:.4f}, "
                f"y={target_pose.position.y:.4f}, "
                f"z={target_pose.position.z:.4f}"
            )

            # Publish selected target pose
            self.publish_selected_block(target_pose)

            # Allow PickAndDrop time to receive the target pose.
            time.sleep(0.3)

            # Execute manipulation
            ok = await self.call_pick_and_drop()

            if not ok:
                self.get_logger().error(
                    "PickAndDrop failed during reset"
                )

                goal_handle.abort()

                return self.make_result(
                    False,
                    "PickAndDrop failed"
                )

            picked_count += 1

            # Clear stale perception state so we wait for a fresh update after the arm moves.
            self.latest_blocks = None
            self.latest_blocks_time = None

            # Give perception time to refresh
            time.sleep(1.0)

        # Safety stop after max attempts
        self.get_logger().warn(
            f"Stopped after max_attempts={max_attempts}. "
            f"Picked {picked_count} blocks."
        )

        goal_handle.succeed()

        return self.make_result(
            True,
            f"Reset stopped after max attempts. "
            f"Picked {picked_count} blocks.",
        )


def main(args=None):
    """
    ROS2 entry point.
    """
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