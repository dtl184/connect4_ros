#!/usr/bin/env python3

"""
Tic-Tac-Toe referee node.

This node acts as a game referee that:
    1. Listens to AprilTag-based board perception.
    2. Converts detected blocks into a Tic-Tac-Toe board state.
    3. Detects wins for either player.
    4. Requires multiple consecutive win detections for stability.
    5. Automatically sends a ResetBoard action after a confirmed win.

ROS INTERFACES
---------------

SUBSCRIBES:
    /connect4/detected_block_poses
        Type: connect4_msgs/msg/DetectedBlockArray

ACTION CLIENT:
    /connect4/reset_board
        Type: connect4_msgs/action/ResetBoard

Board Representation
--------------------

Board cells contain:
    0 -> EMPTY
    1 -> Player 1
    2 -> Player 2

Squares are numbered:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        edge of table is here
"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from connect4_msgs.msg import DetectedBlockArray
from connect4_msgs.action import ResetBoard


class TicTacToeNode(Node):
    """
    Tic-Tac-Toe referee node.
    """

    def __init__(self):
        super().__init__("tic_tac_toe_node")

        # AprilTag ownership
        # Player 1 uses tags 0-3
        # Player 2 uses tags 4-9
        self.player1_tags = {0, 1, 2, 3}
        self.player2_tags = {4, 5, 6, 7, 9}

        self.block_topic = "/connect4/detected_block_poses"

        self.reset_action_name = "/connect4/reset_board"

        self.x_row_split_1 = 0.075
        self.x_row_split_2 = 0.145

        self.y_col_split_1 = 0.060
        self.y_col_split_2 = 0.140

        self.board = [
            [0 for _ in range(3)]
            for _ in range(3)
        ]
        self.reset_client = ActionClient(
            self,
            ResetBoard,
            self.reset_action_name
        )


        self.sub = self.create_subscription(
            DetectedBlockArray,
            self.block_topic,
            self.blocks_callback,
            10
        )

        # Uses perception stabilization from player node to detect a winner
        self.win_candidate = None

        self.win_counter = 0

        self.frames_required_for_reset = 5

        self.reset_sent = False

        self.get_logger().info("Tic Tac Toe referee node started")

        self.get_logger().info(
            f"Listening on {self.block_topic}"
        )

        self.get_logger().info(
            f"Reset action: {self.reset_action_name}"
        )

    def get_player(self, tag_id: int) -> int:
        """
        Determine which player owns an april tag
        """
        if tag_id in self.player1_tags:
            return 1

        if tag_id in self.player2_tags:
            return 2

        return 0

    def pose_to_cell(self, x: float, y: float):
        """
        Convert planar board coordinates into
        a Tic-Tac-Toe board cell.
        """

        # Determine row from x coordinate
        if x < self.x_row_split_1:
            row = 0

        elif x < self.x_row_split_2:
            row = 1

        else:
            row = 2

        # Determine column from y coordinate
        if y < self.y_col_split_1:
            col = 2

        elif y < self.y_col_split_2:
            col = 1

        else:
            col = 0

        return row, col

    def blocks_callback(self, msg: DetectedBlockArray):
        """
        Main perception callback.

        This callback:
            1. Builds a board from detected blocks.
            2. Prints the current board.
            3. Detects wins.
            4. Stabilizes perception of win detection.
            5. Sends a ResetBoard action when a win is confirmed.
        """

        # Ignore perception while reset is active
        if self.reset_sent:
            return

        # Clear board before rebuilding from perception
        self.board = [
            [0 for _ in range(3)]
            for _ in range(3)
        ]

        # Convert perception detections into board state
        for block in msg.blocks:

            player = self.get_player(block.id)

            # Ignore unknown tag IDs
            if player == 0:
                self.get_logger().warn(
                    f"Ignoring unknown tag ID {block.id}"
                )

                continue

            x = block.pose.position.x
            y = block.pose.position.y

            row, col = self.pose_to_cell(x, y)

            # Reject duplicate block placements
            if self.board[row][col] != 0:
                self.get_logger().warn(
                    f"Cell ({row}, {col}) already occupied. "
                    f"Existing={self.board[row][col]}, "
                    f"new player={player}, "
                    f"tag={block.id}"
                )

                continue

            self.board[row][col] = player

            self.get_logger().info(
                f"Tag {block.id} -> Player {player} -> "
                f"x={x:.3f}, y={y:.3f} -> "
                f"cell ({row}, {col})"
            )

        self.print_board()

        winner = self.check_winner()

        # No winner detected
        if winner is None:
            self.win_candidate = None
            self.win_counter = 0
            return

        # Stabilize perception, only accept a winning board if we see it for a few frames
        if self.win_candidate == winner:
            self.win_counter += 1

        else:
            self.win_candidate = winner
            self.win_counter = 1

        self.get_logger().info(
            f"Player {winner} win detected "
            f"{self.win_counter}/"
            f"{self.frames_required_for_reset}"
        )

        if self.win_counter >= self.frames_required_for_reset:

            self.get_logger().info(
                f"Player {winner} wins. "
                f"Sending reset board action."
            )

            self.send_reset_board()

    def check_winner(self):
        """
        Check whether either player has won.
        """
        lines = []

        # Rows
        lines.extend(self.board)

        # Columns
        for col in range(3):
            lines.append([
                self.board[0][col],
                self.board[1][col],
                self.board[2][col],
            ])

        # Diagonals
        lines.append([
            self.board[0][0],
            self.board[1][1],
            self.board[2][2],
        ])

        lines.append([
            self.board[0][2],
            self.board[1][1],
            self.board[2][0],
        ])

        # Check winning lines
        for line in lines:

            if line == [1, 1, 1]:
                return 1

            if line == [2, 2, 2]:
                return 2

        return None

    def send_reset_board(self):
        """
        Send a ResetBoard action
        """

        if self.reset_sent:
            return

        self.reset_sent = True

        if not self.reset_client.wait_for_server(timeout_sec=2.0):

            self.get_logger().error(
                "ResetBoard action server not available"
            )

            self.reset_sent = False

            return

        goal_msg = ResetBoard.Goal()

        future = self.reset_client.send_goal_async(goal_msg)

        future.add_done_callback(
            self.reset_goal_response_callback
        )

    def reset_goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:

            self.get_logger().error(
                "ResetBoard goal rejected"
            )

            self.reset_sent = False

            return

        self.get_logger().info(
            "ResetBoard goal accepted"
        )

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            self.reset_result_callback
        )

    def reset_result_callback(self, future):
        self.get_logger().info(
            "ResetBoard action finished"
        )

        self.reset_sent = False

    def print_board(self):
        symbols = {
            0: ".",
            1: "X",
            2: "O",
        }

        rows = []

        for row in self.board:
            rows.append(
                " ".join(symbols[cell] for cell in row)
            )

        self.get_logger().info(
            "\n" + "\n".join(rows)
        )


def main(args=None):
    """
    ROS2 entry point
    """
    rclpy.init(args=args)

    node = TicTacToeNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()