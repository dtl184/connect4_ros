#!/usr/bin/env python3

"""
Tic-Tac-Toe robot player node (custom node)

This node:
    1. Listens to AprilTag-based board perception.
    2. Converts detected blocks into a Tic-Tac-Toe board state.
    3. Validates human and robot moves.
    4. Uses minimax to choose optimal robot moves.
    5. Sends pick-and-place goals to the manipulation system.
    6. Automatically resets the board after wins or draws.

ROS INTERFACES
-------------------
SUBSCRIBES:
    /connect4/detected_block_poses
        Type: connect4_msgs/msg/DetectedBlockArray

ACTION CLIENT:
    /connect4/pick_and_place
        Type: connect4_msgs/action/PickAndPlace

    /connect4/reset_board
        Type: connect4_msgs/action/ResetBoard

The board is represented as follows:
--------------------

Board cells contain:
    EMPTY = 0
    HUMAN = 1
    ROBOT = 2

Squares are numbered:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        edge of table is here

Robot Logic
-----------

The robot:
    - waits for a valid human move,
    - computes an optimal response using minimax,
    - physically places a block using the manipulator,
    - waits for perception confirmation,
    - continues until game over.
"""

import copy
from typing import Optional, Tuple, List

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from connect4_msgs.msg import DetectedBlockArray
from connect4_msgs.action import PickAndPlace, ResetBoard, TurtleDeliver


EMPTY = 0
HUMAN = 1
ROBOT = 2


class TicTacToeRobotNode(Node):
    """
    Autonomous Tic-Tac-Toe robot player.
    """

    def __init__(self):

        super().__init__("tic_tac_toe_robot_node")

        # Set which april tag ids belong to human blocks and robot blocks
        self.player1_tags = {0, 1, 2, 3}
        self.player2_tags = {4, 5, 6, 7, 8, 9}

        self.block_topic = "/connect4/detected_block_poses"

        self.pick_and_place_action_name = "/connect4/pick_and_place"

        self.reset_action_name = "/connect4/reset_board"

        # Harcoded points where to split the board in the camera's image along tic-tac-toe lines
        self.x_row_split_1 = 0.075
        self.x_row_split_2 = 0.145

        self.y_col_split_1 = 0.060
        self.y_col_split_2 = 0.140

        # Board state is initially empty
        self.current_board = [
            [EMPTY for _ in range(3)]
            for _ in range(3)
        ]

        # Store the last valid board state
        self.last_accepted_board = [
            [EMPTY for _ in range(3)]
            for _ in range(3)
        ]


        # We need to stabilize perception, only detect blocks when the image is stable
        # So we don't detect human hands, etc.
        # This is the most recent repeated board observation.
        self.stable_candidate_board = None

        # Number of consecutive frames matching a candidate board
        self.stable_count = 0

        # We must see 5 stable frames before accepting
        self.frames_required_stable = 5

        # Helpful status flags
        self.robot_busy = False
        self.game_over = False
        self.reset_sent = False

        # These are the hardcoded positions of the robot's blocks.
        # After each human turn, the robot goes to the next position to get a block for its turn
        self.next_supply_index = 0
        self.pending_robot_square = None
        self.robot_supply_poses = [
            self.make_pose(-0.173, -0.250, 0.040),
            self.make_pose(-0.111, -0.250, 0.040),
            self.make_pose(-0.030, -0.250, 0.040),
            self.make_pose(0.033, -0.250, 0.040),
        ]

        # Hardcoded positions on the board, these are where the blocks will be placed
        self.board_place_poses = {
            0: self.make_pose(-0.104, -0.481, 0.040),
            1: self.make_pose(-0.106, -0.428, 0.040),
            2: self.make_pose(-0.106, -0.366, 0.040),

            3: self.make_pose(-0.047, -0.489, 0.040),
            4: self.make_pose(-0.056, -0.435, 0.040),
            5: self.make_pose(-0.055, -0.372, 0.040),

            6: self.make_pose(-0.001, -0.491, 0.040),
            7: self.make_pose(0.009, -0.426, 0.040),
            8: self.make_pose(-0.005, -0.375, 0.040),
        }

        self.pick_and_place_client = ActionClient(
            self,
            PickAndPlace,
            self.pick_and_place_action_name,
        )

        self.reset_client = ActionClient(
            self,
            ResetBoard,
            self.reset_action_name,
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
            10,
        )

        self.get_logger().info("Tic Tac Toe robot node started")

        self.get_logger().info(f"Robot is player {ROBOT}")

        self.get_logger().info(f"Listening on {self.block_topic}")

        self.get_logger().info(
            f"Pick/place action: {self.pick_and_place_action_name}"
        )

        self.get_logger().info(
            f"Reset action: {self.reset_action_name}"
        )

    def make_pose(
        self,
        x: float,
        y: float,
        z: float
    ) -> PoseStamped:
        pose = PoseStamped()

        pose.header.frame_id = "base"

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        # Gripper will always stay in the same orientation
        pose.pose.orientation.x = -0.012
        pose.pose.orientation.y = 1.000
        pose.pose.orientation.z = 0.021
        pose.pose.orientation.w = 0.014

        return pose

    def get_player(self, tag_id: int) -> int:
        """
        Determine which player owns a detected AprilTag.
        """
        if tag_id in self.player1_tags:
            return HUMAN

        if tag_id in self.player2_tags:
            return ROBOT

        return EMPTY

    def pose_to_cell(
        self,
        x: float,
        y: float
    ) -> Tuple[int, int]:
        """
        Convert planar coordinates into a Tic-Tac-Toe cell.
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
        Perception callback function
        """
        # Ignore updates while robot is moving/resetting
        if self.robot_busy or self.reset_sent:
            return

        # Build board from detected blocks
        observed_board = self.build_board_from_blocks(msg)

        # Get stable perception updates
        if observed_board == self.stable_candidate_board:
            self.stable_count += 1
        else:
            self.stable_candidate_board = copy.deepcopy(observed_board)
            self.stable_count = 1
        # No stable board detected, return
        if self.stable_count < self.frames_required_stable:
            return

        self.current_board = copy.deepcopy(observed_board)

        # Ignore unchanged board
        if self.current_board == self.last_accepted_board:
            return

        self.get_logger().info("Stable board update accepted:")

        self.print_board(self.current_board)

        # Waiting for robot move confirmation
        if self.pending_robot_square is not None:

            if self.valid_robot_move(
                self.last_accepted_board,
                self.current_board,
                self.pending_robot_square,
            ):
                self.get_logger().info(
                    f"Confirmed robot move at square "
                    f"{self.pending_robot_square}"
                )

                self.last_accepted_board = copy.deepcopy(
                    self.current_board
                )

                self.pending_robot_square = None

                if self.handle_game_over_if_needed():
                    return

                return

            self.get_logger().warn(
                "Waiting for perception to confirm robot move. "
                "Ignoring update."
            )

            return

        # Validate human move
        if not self.valid_human_move(
            self.last_accepted_board,
            self.current_board,
        ):
            self.get_logger().warn(
                "Board changed, but it was not exactly "
                "one new move. Ignoring."
            )

            return

        self.last_accepted_board = copy.deepcopy(self.current_board)

        # Game-over check
        if self.handle_game_over_if_needed():
            return

        # Choose robot move
        robot_square = self.choose_robot_move(self.current_board)

        if robot_square is None:
            self.get_logger().info("No legal robot move available.")

            self.game_over = True

            self.send_reset_board()
<<<<<<< HEAD

=======
            goal = TurtleDeliver.Goal()
            goal.x = 1.0
            goal.y = 0.0
            goal.yaw = 0.0

            self.turtle_client.wait_for_server()
            self.turtle_client.send_goal_async(goal)
>>>>>>> 3c4320a35d110b0c840f03d63b6ac0b503829f05
            return

        self.get_logger().info(
            f"Robot chose square {robot_square}"
        )

        self.send_pick_and_place(robot_square)

    def handle_game_over_if_needed(self) -> bool:
        """
        Check if someone won or if both players drew
        """
        winner = self.check_winner(self.current_board)

        if winner is not None:
            self.get_logger().info(
                f"Game over. Player {winner} won."
            )

            self.game_over = True

            self.send_reset_board()

            return True

        if self.is_draw(self.current_board):
            self.get_logger().info("Game over. Draw.")

            self.game_over = True

            self.send_reset_board()

            return True

        return False

    def build_board_from_blocks(
        self,
        msg: DetectedBlockArray
    ) -> List[List[int]]:
        """
        Construct a board state from perception detections.
        """
        board = [
            [EMPTY for _ in range(3)]
            for _ in range(3)
        ]

        for block in msg.blocks:

            player = self.get_player(block.id)

            if player == EMPTY:
                self.get_logger().warn(
                    f"Ignoring unknown tag ID {block.id}"
                )

                continue

            row, col = self.pose_to_cell(
                block.pose.position.x,
                block.pose.position.y,
            )

            # Reject placements into the same location as another block
            if board[row][col] != EMPTY:
                self.get_logger().warn(
                    f"Cell ({row}, {col}) already occupied. "
                    f"Existing={board[row][col]}, "
                    f"new={player}, "
                    f"tag={block.id}"
                )

                continue

            board[row][col] = player

        return board

    def send_reset_board(self):
        """
        Send a ResetBoard action
        """
        if self.reset_sent:
            return

        self.reset_sent = True
        self.robot_busy = True

        if not self.reset_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error(
                "ResetBoard action server not available"
            )

            self.reset_sent = False
            self.robot_busy = False

            return

        self.get_logger().info("Sending ResetBoard action")

        goal_msg = ResetBoard.Goal()

        future = self.reset_client.send_goal_async(goal_msg)

        future.add_done_callback(
            self.reset_goal_response_callback
        )

    def reset_goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error("ResetBoard goal rejected")

            self.reset_sent = False
            self.robot_busy = False

            return

        self.get_logger().info("ResetBoard goal accepted")

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            self.reset_result_callback
        )

    def reset_result_callback(self, future):
        result = future.result().result

        success = getattr(result, "success", True)

        message = getattr(result, "message", "")

        self.get_logger().info(
            f"ResetBoard finished: "
            f"success={success}, "
            f"message={message}"
        )

        # Clear all board/perception state
        self.current_board = [
            [EMPTY for _ in range(3)]
            for _ in range(3)
        ]

        self.last_accepted_board = [
            [EMPTY for _ in range(3)]
            for _ in range(3)
        ]

        self.stable_candidate_board = None

        self.stable_count = 0

        self.pending_robot_square = None

        self.next_supply_index = 0

        self.robot_busy = False
        self.game_over = False
        self.reset_sent = False

        self.get_logger().info("Ready for next game.")

    def valid_human_move(self, old_board, new_board) -> bool:
        """
        Validate a human move.

        A valid human move has:
            -Exactly one human piece added.
            -No robot pieces added.
            -No pieces removed.
            -No illegal modifications.
        """
        human_added = 0
        robot_added = 0
        removed = 0
        changed_badly = 0

        for r in range(3):
            for c in range(3):

                old = old_board[r][c]
                new = new_board[r][c]

                if old == new:
                    continue

                if old == EMPTY and new == HUMAN:
                    human_added += 1

                elif old == EMPTY and new == ROBOT:
                    robot_added += 1

                elif old != EMPTY and new == EMPTY:
                    removed += 1

                else:
                    changed_badly += 1

        return (
            human_added == 1
            and robot_added == 0
            and removed == 0
            and changed_badly == 0
        )

    def valid_robot_move(
        self,
        old_board,
        new_board,
        expected_square: int,
    ) -> bool:
        """
        Validate a robot move.

        Compares current previous board state to ensure exactly one block was moved
        """
        expected_row, expected_col = self.square_to_row_col(
            expected_square
        )

        robot_added = 0
        human_added = 0
        removed = 0
        changed_badly = 0

        for r in range(3):
            for c in range(3):

                old = old_board[r][c]
                new = new_board[r][c]

                if old == new:
                    continue

                if old == EMPTY and new == ROBOT:
                    robot_added += 1

                    if r != expected_row or c != expected_col:
                        changed_badly += 1

                elif old == EMPTY and new == HUMAN:
                    human_added += 1

                elif old != EMPTY and new == EMPTY:
                    removed += 1

                else:
                    changed_badly += 1

        return (
            robot_added == 1
            and human_added == 0
            and removed == 0
            and changed_badly == 0
        )

    def choose_robot_move(
        self,
        board
    ) -> Optional[int]:
        """
        Choose the robot's optimal move using minimax.
        """
        best_score = -999

        best_square = None

        for square in self.empty_squares(board):

            r, c = self.square_to_row_col(square)

            board[r][c] = ROBOT

            score = self.minimax(
                board,
                maximizing=False
            )

            board[r][c] = EMPTY

            if score > best_score:
                best_score = score
                best_square = square

        return best_square

    def minimax(
        self,
        board,
        maximizing: bool
    ) -> int:
        """
        Implements minimax search. 
        We assume that: robot will always choose moves maximizing the score and 
        the human will always choose moves minimizing the score.
        """
        winner = self.check_winner(board)

        # Rewards for human or robot winning
        if winner == ROBOT:
            return 10

        if winner == HUMAN:
            return -10

        if self.is_draw(board):
            return 0

        # Robot turn
        if maximizing:

            # Start with a very bad score and try to do better
            best_score = -999

            # Try all the empty squares
            for square in self.empty_squares(board):
                
                # try placing the block in a particular square
                r, c = self.square_to_row_col(square)

                board[r][c] = ROBOT

                # Call minimax on this simulated move to see how the human responds
                score = self.minimax(
                    board,
                    maximizing=False
                )

                # Backtrack and choose the move with the highest score
                board[r][c] = EMPTY

                best_score = max(best_score, score)

            return best_score

        # Human turn
        best_score = 999

        for square in self.empty_squares(board):

            # Human tries a move
            r, c = self.square_to_row_col(square)

            board[r][c] = HUMAN

            # See what the robot does
            score = self.minimax(
                board,
                maximizing=True
            )

            # Choose the move that minimizes the score
            board[r][c] = EMPTY

            best_score = min(best_score, score)

        return best_score

    def empty_squares(self, board) -> List[int]:
        """
        Return all currently empty board squares.
        """
        return [
            self.row_col_to_square(r, c)
            for r in range(3)
            for c in range(3)
            if board[r][c] == EMPTY
        ]

    def row_col_to_square(
        self,
        row: int,
        col: int
    ) -> int:
        """
        Convert (row, col) into board square index.
        """
        return row * 3 + col

    def square_to_row_col(
        self,
        square: int
    ) -> Tuple[int, int]:
        """
        Convert board square index into (row, col).
        """
        return square // 3, square % 3

    def check_winner(self, board) -> Optional[int]:
        """
        Check for a winning player.
        """
        lines = []

        # Rows
        lines.extend(board)

        # Columns
        for col in range(3):
            lines.append([
                board[0][col],
                board[1][col],
                board[2][col]
            ])

        # Diagonals
        lines.append([
            board[0][0],
            board[1][1],
            board[2][2]
        ])

        lines.append([
            board[0][2],
            board[1][1],
            board[2][0]
        ])

        for line in lines:

            if line == [HUMAN, HUMAN, HUMAN]:
                return HUMAN

            if line == [ROBOT, ROBOT, ROBOT]:
                return ROBOT

        return None

    def is_draw(self, board) -> bool:
        """
        Determine whether the game is a draw.
        """
        return (
            self.check_winner(board) is None
            and len(self.empty_squares(board)) == 0
        )

    def send_pick_and_place(self, square: int):
        if self.next_supply_index >= len(self.robot_supply_poses):
            self.get_logger().error(
                "No more hardcoded robot supply poses available."
            )

            return

        pickup_pose = copy.deepcopy(
            self.robot_supply_poses[self.next_supply_index]
        )

        place_pose = copy.deepcopy(
            self.board_place_poses[square]
        )

        self.get_logger().info(
            f"Picking block from location "
            f"{pickup_pose.pose.position.x}, "
            f"{pickup_pose.pose.position.y}"
        )

        now = self.get_clock().now().to_msg()

        pickup_pose.header.stamp = now
        place_pose.header.stamp = now

        self.next_supply_index += 1

        self.pending_robot_square = square

        self.robot_busy = True

        if not self.pick_and_place_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error(
                "PickAndPlace action server not available"
            )

            self.robot_busy = False

            self.pending_robot_square = None

            self.next_supply_index -= 1

            return

        goal_msg = PickAndPlace.Goal()

        goal_msg.pickup_pose = pickup_pose
        goal_msg.place_pose = place_pose

        self.get_logger().info(
            f"Sending PickAndPlace: "
            f"supply index {self.next_supply_index - 1} "
            f"-> board square {square}"
        )

        future = self.pick_and_place_client.send_goal_async(goal_msg)

        future.add_done_callback(
            self.pick_and_place_goal_response_callback
        )

    def pick_and_place_goal_response_callback(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error(
                "PickAndPlace goal rejected"
            )

            self.robot_busy = False

            self.pending_robot_square = None

            self.next_supply_index -= 1

            return

        self.get_logger().info(
            "PickAndPlace goal accepted"
        )

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            self.pick_and_place_result_callback
        )

    def pick_and_place_result_callback(self, future):
        self.robot_busy = False

        result = future.result().result

        self.get_logger().info(
            f"PickAndPlace finished: "
            f"success={result.success}, "
            f"message={result.message}"
        )

        if not result.success:
            self.pending_robot_square = None

            self.next_supply_index -= 1

            return

        self.get_logger().info(
            "Waiting for perception to confirm robot move."
        )

    def print_board(self, board):
        """
        Print a human-readable board to the ROS log.
        """
        symbols = {
            EMPTY: ".",
            HUMAN: "X",
            ROBOT: "O",
        }

        rows = [
            " ".join(symbols[cell] for cell in row)
            for row in board
        ]

        self.get_logger().info(
            "\n" + "\n".join(rows)
        )


def main(args=None):
    """
    ROS2 entry point.
    """
    rclpy.init(args=args)

    node = TicTacToeRobotNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()