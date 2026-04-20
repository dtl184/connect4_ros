import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from connect4_msgs.msg import BoardState, Winner
from connect4_msgs.action import DeliverBlock, ResetBoard


class RefereeNode(Node):
    def __init__(self):
        super().__init__('referee_node')

        cb_group = ReentrantCallbackGroup()

        self.board_state_sub = self.create_subscription(
            BoardState,
            '/connect4/board_state',
            self.board_state_callback,
            10,
            callback_group=cb_group,
        )

        self.winner_pub = self.create_publisher(Winner, '/connect4/winner', 10)

        self.deliver_block_client = ActionClient(
            self, DeliverBlock, '/connect4/deliver_block', callback_group=cb_group
        )

        self.reset_board_client = ActionClient(
            self, ResetBoard, '/connect4/reset_board', callback_group=cb_group
        )

        self.previous_board_state = None
        self.current_player = 1
        self.awaiting_move = False
        self._game_started = False

        # Kick off first block delivery a few seconds after startup so action
        # servers have time to come up.
        self._start_timer = self.create_timer(
            3.0, self._start_game_once, callback_group=cb_group
        )

        self.get_logger().info('RefereeNode started')

    def _start_game_once(self):
        if self._game_started:
            return
        self._game_started = True
        self._start_timer.cancel()
        self.get_logger().info('Starting game — delivering block to player 1')
        self.send_deliver_block_goal(1)

    def board_state_callback(self, msg: BoardState) -> None:
        if not self.awaiting_move:
            return

        self.get_logger().info('Received board state — evaluating move')

        if not self.is_legal_move(self.previous_board_state, msg):
            self.get_logger().warn('Illegal move detected (more than one block changed)')

        if self.is_winner(msg):
            winner_msg = Winner()
            winner_msg.winner = self.current_player
            self.winner_pub.publish(winner_msg)
            self.get_logger().info('Player %d wins!' % self.current_player)
            self.awaiting_move = False
            self.send_reset_board_goal(msg)
        else:
            self.previous_board_state = msg
            self.current_player = 2 if self.current_player == 1 else 1
            self.awaiting_move = False
            self.send_deliver_block_goal(self.current_player)

    def is_winner(self, board_state: BoardState) -> bool:
        cells = board_state.cells
        rows, cols = 6, 7

        def get(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return cells[r * cols + c]
            return -1

        for player in (1, 2):
            for r in range(rows):
                for c in range(cols):
                    if get(r, c) != player:
                        continue
                    # horizontal, vertical, diagonal down-right, diagonal down-left
                    for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                        if all(get(r + k * dr, c + k * dc) == player for k in range(4)):
                            return True
        return False

    def is_legal_move(self, previous: BoardState, current: BoardState) -> bool:
        if previous is None:
            return True
        diff = sum(1 for a, b in zip(previous.cells, current.cells) if a != b)
        return diff == 1


    # Deliver Block Action Client

    def send_deliver_block_goal(self, player: int) -> None:
        self.get_logger().info('Sending DeliverBlock goal for player %d' % player)

        if not self.deliver_block_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('DeliverBlock server not available')
            return

        goal_msg = DeliverBlock.Goal()
        goal_msg.player = player
        future = self.deliver_block_client.send_goal_async(goal_msg)
        future.add_done_callback(self._deliver_goal_response_cb)

    def _deliver_goal_response_cb(self, future):
        gh = future.result()
        if not gh.accepted:
            self.get_logger().error('DeliverBlock goal rejected')
            return
        self.get_logger().info('DeliverBlock goal accepted')
        gh.get_result_async().add_done_callback(self._deliver_result_cb)

    def _deliver_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            'DeliverBlock result: success=%s, msg=%s' % (result.success, result.message)
        )
        self.awaiting_move = True


    # Reset Board Action Client

    def send_reset_board_goal(self, board_state: BoardState) -> None:
        self.get_logger().info('Sending ResetBoard goal')

        if not self.reset_board_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('ResetBoard server not available')
            return

        goal_msg = ResetBoard.Goal()
        goal_msg.final_board_state = board_state
        future = self.reset_board_client.send_goal_async(goal_msg)
        future.add_done_callback(self._reset_goal_response_cb)

    def _reset_goal_response_cb(self, future):
        gh = future.result()
        if not gh.accepted:
            self.get_logger().error('ResetBoard goal rejected')
            return
        self.get_logger().info('ResetBoard goal accepted')
        gh.get_result_async().add_done_callback(self._reset_result_cb)

    def _reset_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            'ResetBoard result: success=%s, msg=%s' % (result.success, result.message)
        )
        self.current_player = 1
        self.previous_board_state = None
        self.get_logger().info('Board reset complete — starting new game')
        self.send_deliver_block_goal(1)


def main(args=None):
    rclpy.init(args=args)
    node = RefereeNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
