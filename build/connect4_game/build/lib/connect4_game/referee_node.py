import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from connect4_msgs.msg import BoardState, Winner
from connect4_msgs.action import DeliverBlock, ResetBoard


class RefereeNode(Node):
    def __init__(self):
        super().__init__('referee_node')

        self.board_state_sub = self.create_subscription(
            BoardState,
            '/connect4/board_state',
            self.board_state_callback,
            10
        )

        self.winner_pub = self.create_publisher(
            Winner,
            '/connect4/winner',
            10
        )

        self.deliver_block_client = ActionClient(
            self,
            DeliverBlock,
            '/connect4/deliver_block'
        )

        self.reset_board_client = ActionClient(
            self,
            ResetBoard,
            '/connect4/reset_board'
        )

        self.previous_board_state = None
        self.current_player = 1
        self.game_over = False
        self.waiting_for_move = False

        self.rows = 6
        self.cols = 7

        self.get_logger().info('RefereeNode started')

        # deliver the first block at startup
        self.send_deliver_block_goal(self.current_player)
        self.waiting_for_move = True

    def board_state_callback(self, msg: BoardState) -> None:
        self.get_logger().info('Received board state')

        if self.game_over:
            return

        # first board state received: just store it
        if self.previous_board_state is None:
            self.previous_board_state = msg
            return

        # ignore repeated identical board states
        if msg.cells == self.previous_board_state.cells:
            self.get_logger().info('Board unchanged, ignoring')
            return

        # legality check
        if not self.is_legal_move(self.previous_board_state, msg):
            self.get_logger().warn('Illegal move detected')
            self.previous_board_state = msg
            return

        # winner check
        if self.is_winner(msg, self.current_player):
            self.get_logger().info(f'Player {self.current_player} wins')
            self.game_over = True

            winner_msg = Winner()
            winner_msg.winner = self.current_player
            self.winner_pub.publish(winner_msg)

            self.send_reset_board_goal(msg)
        else:
            # move accepted, switch players
            self.previous_board_state = msg
            self.current_player = 2 if self.current_player == 1 else 1
            self.send_deliver_block_goal(self.current_player)

    def is_winner(self, board_state: BoardState, player: int) -> bool:
        board = board_state.cells

        def get_cell(r, c):
            return board[r * self.cols + c]

        for r in range(self.rows):
            for c in range(self.cols):
                if get_cell(r, c) != player:
                    continue

                # horizontal
                if c <= self.cols - 4:
                    if all(get_cell(r, c + i) == player for i in range(4)):
                        return True

                # vertical
                if r <= self.rows - 4:
                    if all(get_cell(r + i, c) == player for i in range(4)):
                        return True

                # diagonal down-right
                if r <= self.rows - 4 and c <= self.cols - 4:
                    if all(get_cell(r + i, c + i) == player for i in range(4)):
                        return True

                # diagonal down-left
                if r <= self.rows - 4 and c >= 3:
                    if all(get_cell(r + i, c - i) == player for i in range(4)):
                        return True

        return False

    def is_legal_move(self, previous: BoardState, current: BoardState) -> bool:
        prev = previous.cells
        curr = current.cells

        if len(prev) != self.rows * self.cols or len(curr) != self.rows * self.cols:
            self.get_logger().warn('Board size incorrect')
            return False

        changed_indices = [i for i in range(len(prev)) if prev[i] != curr[i]]

        # exactly one cell should change
        if len(changed_indices) != 1:
            self.get_logger().warn(f'Illegal move: expected 1 changed cell, got {len(changed_indices)}')
            return False

        idx = changed_indices[0]

        # must go from empty to current player's piece
        if prev[idx] != 0:
            self.get_logger().warn('Illegal move: changed cell was not empty before')
            return False

        if curr[idx] != self.current_player:
            self.get_logger().warn('Illegal move: wrong player piece placed')
            return False

        row = idx // self.cols
        col = idx % self.cols

        # connect four gravity check:
        # every filled piece must either be in bottom row or have a filled cell below it
        if row < self.rows - 1:
            below_idx = (row + 1) * self.cols + col
            if curr[below_idx] == 0:
                self.get_logger().warn('Illegal move: floating piece')
                return False

        return True

    def send_deliver_block_goal(self, player: int) -> None:
        self.get_logger().info(f'Sending DeliverBlock goal for player {player}')

        if not self.deliver_block_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error('DeliverBlock action server not available')
            return

        goal_msg = DeliverBlock.Goal()
        goal_msg.player = player

        future = self.deliver_block_client.send_goal_async(goal_msg)
        future.add_done_callback(self.deliver_block_goal_response_callback)

    def deliver_block_goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('DeliverBlock goal rejected')
            return

        self.get_logger().info('DeliverBlock goal accepted')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.deliver_block_result_callback)

    def deliver_block_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'DeliverBlock result: success={result.success}, message="{result.message}"')

    def send_reset_board_goal(self, board_state: BoardState) -> None:
        self.get_logger().info('Sending ResetBoard goal')

        if not self.reset_board_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error('ResetBoard action server not available')
            return

        goal_msg = ResetBoard.Goal()
        goal_msg.final_board_state = board_state

        future = self.reset_board_client.send_goal_async(goal_msg)
        future.add_done_callback(self.reset_board_goal_response_callback)

    def reset_board_goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('ResetBoard goal rejected')
            return

        self.get_logger().info('ResetBoard goal accepted')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.reset_board_result_callback)

    def reset_board_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'ResetBoard result: success={result.success}, message="{result.message}"')

        # start new game
        self.previous_board_state = None
        self.current_player = 1
        self.game_over = False

        self.send_deliver_block_goal(self.current_player)


def main(args=None):
    rclpy.init(args=args)
    node = RefereeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()