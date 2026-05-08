#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from connect4_msgs.msg import DetectedBlockArray
from connect4_msgs.action import ResetBoard, TurtleDeliver


class TicTacToeNode(Node):
    def __init__(self):
        super().__init__("tic_tac_toe_node")

        self.player1_tags = {0, 1, 2, 3}

        # Placeholder until you make player 2 tags
        self.player2_tags = {4,5,6,7,9}

        self.block_topic = "/connect4/detected_block_poses"
        self.reset_action_name = "/connect4/reset_board"

        # These are based on your earlier calibrated board coordinates.
        # x determines row: top, middle, bottom
        # y determines col: left, middle, right
        self.x_row_split_1 = 0.075
        self.x_row_split_2 = 0.145

        self.y_col_split_1 = 0.060
        self.y_col_split_2 = 0.140

        self.board = [[0 for _ in range(3)] for _ in range(3)]

        self.reset_client = ActionClient(
            self,
            ResetBoard,
            self.reset_action_name
        )
        self.turtle_client = ActionClient(
            self,
            TurtleDeliver,
            "/connect4/turtle_deliver",
        )

        self.sub = self.create_subscription(
            DetectedBlockArray,
            self.block_topic,
            self.blocks_callback,
            10
        )

        self.win_candidate = None
        self.win_counter = 0
        self.frames_required_for_reset = 5
        self.reset_sent = False

        self.get_logger().info("Tic Tac Toe node started")
        self.get_logger().info(f"Listening on {self.block_topic}")
        self.get_logger().info(f"Reset action: {self.reset_action_name}")

    def get_player(self, tag_id: int) -> int:
        if tag_id in self.player1_tags:
            return 1
        if tag_id in self.player2_tags:
            return 2
        return 0

    def pose_to_cell(self, x: float, y: float):
        if x < self.x_row_split_1:
            row = 0
        elif x < self.x_row_split_2:
            row = 1
        else:
            row = 2

        if y < self.y_col_split_1:
            col = 2
        elif y < self.y_col_split_2:
            col = 1
        else:
            col = 0

        return row, col

    def blocks_callback(self, msg: DetectedBlockArray):
        if self.reset_sent:
            return

        self.board = [[0 for _ in range(3)] for _ in range(3)]

        for block in msg.blocks:
            player = self.get_player(block.id)

            if player == 0:
                self.get_logger().warn(f"Ignoring unknown tag ID {block.id}")
                continue

            x = block.pose.position.x
            y = block.pose.position.y

            row, col = self.pose_to_cell(x, y)

            if self.board[row][col] != 0:
                self.get_logger().warn(
                    f"Cell ({row}, {col}) already occupied. "
                    f"Existing={self.board[row][col]}, new player={player}, tag={block.id}"
                )
                continue

            self.board[row][col] = player

            self.get_logger().info(
                f"Tag {block.id} -> Player {player} -> "
                f"x={x:.3f}, y={y:.3f} -> cell ({row}, {col})"
            )

        self.print_board()

        winner = self.check_winner()

        if winner is None:
            self.win_candidate = None
            self.win_counter = 0
            return

        if self.win_candidate == winner:
            self.win_counter += 1
        else:
            self.win_candidate = winner
            self.win_counter = 1

        self.get_logger().info(
            f"Player {winner} win detected "
            f"{self.win_counter}/{self.frames_required_for_reset}"
        )

        if self.win_counter >= self.frames_required_for_reset:
            self.get_logger().info(f"Player {winner} wins. Sending reset board action.")
            self.send_reset_board()
            goal = TurtleDeliver.Goal()
            goal.x = 1.0
            goal.y = 0.0
            goal.yaw = 0.0

            self.turtle_client.wait_for_server()
            self.turtle_client.send_goal_async(goal)

    def check_winner(self):
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

        for line in lines:
            if line == [1, 1, 1]:
                return 1
            if line == [2, 2, 2]:
                return 2

        return None

    def send_reset_board(self):
        self.reset_sent = True

        if not self.reset_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error("ResetBoard action server not available")
            self.reset_sent = False
            return

        goal_msg = ResetBoard.Goal()

        future = self.reset_client.send_goal_async(goal_msg)
        future.add_done_callback(self.reset_goal_response_callback)

    def reset_goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error("ResetBoard goal rejected")
            self.reset_sent = False
            return

        self.get_logger().info("ResetBoard goal accepted")

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.reset_result_callback)

    def reset_result_callback(self, future):
        self.get_logger().info("ResetBoard action finished")

    def print_board(self):
        symbols = {
            0: ".",
            1: "X",
            2: "O",
        }

        rows = []
        for row in self.board:
            rows.append(" ".join(symbols[cell] for cell in row))

        self.get_logger().info("\n" + "\n".join(rows))


def main(args=None):
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