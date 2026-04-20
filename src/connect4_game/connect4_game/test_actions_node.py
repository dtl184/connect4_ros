import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from connect4_msgs.action import DeliverBlock, ResetBoard
from connect4_msgs.msg import BoardState


class TestActionsNode(Node):
    """Exercise DeliverBlock (Nav2) and ResetBoard (MoveIt) action servers."""

    def __init__(self):
        super().__init__('test_actions_node')

        cb = ReentrantCallbackGroup()
        self.deliver_client = ActionClient(
            self, DeliverBlock, '/connect4/deliver_block', callback_group=cb
        )
        self.reset_client = ActionClient(
            self, ResetBoard, '/connect4/reset_board', callback_group=cb
        )

        self._tests_run = False
        self.create_timer(2.0, self._run_tests, callback_group=cb)
        self.get_logger().info('TestActionsNode ready — waiting 2 s before sending goals')

    # ------------------------------------------------------------------ #
    # Test entry-point                                                     #
    # ------------------------------------------------------------------ #

    def _run_tests(self):
        if self._tests_run:
            return
        self._tests_run = True
        self.get_logger().info('=== Connect4 Action Tests START ===')
        self._test_deliver_block(player=1)

    # ------------------------------------------------------------------ #
    # Test 1: DeliverBlock -> Nav2                                        #
    # ------------------------------------------------------------------ #

    def _test_deliver_block(self, player: int):
        self.get_logger().info('[TEST] DeliverBlock: player=%d' % player)

        if not self.deliver_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('[TEST] DeliverBlock server not reachable — skipping to ResetBoard test')
            self._test_reset_board()
            return

        goal = DeliverBlock.Goal()
        goal.player = player
        future = self.deliver_client.send_goal_async(
            goal, feedback_callback=self._deliver_feedback_cb
        )
        future.add_done_callback(self._deliver_response_cb)

    def _deliver_feedback_cb(self, fb_msg):
        self.get_logger().info('[TEST] DeliverBlock feedback: %s' % fb_msg.feedback.status)

    def _deliver_response_cb(self, future):
        gh = future.result()
        if not gh.accepted:
            self.get_logger().error('[TEST] DeliverBlock goal rejected')
            self._test_reset_board()
            return
        self.get_logger().info('[TEST] DeliverBlock goal accepted — waiting for result')
        gh.get_result_async().add_done_callback(self._deliver_result_cb)

    def _deliver_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            '[TEST] DeliverBlock result: success=%s  msg="%s"' % (result.success, result.message)
        )
        self._test_reset_board()

    # ------------------------------------------------------------------ #
    # Test 2: ResetBoard -> MoveIt                                        #
    # ------------------------------------------------------------------ #

    def _test_reset_board(self):
        self.get_logger().info('[TEST] ResetBoard: sending 3-block test board')

        if not self.reset_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('[TEST] ResetBoard server not reachable')
            self._finish()
            return

        # Build a simple test board: three blocks in the bottom row
        board = BoardState()
        board.cells = [0] * 42
        board.cells[35] = 1  # row 5, col 0 — red
        board.cells[36] = 2  # row 5, col 1 — blue
        board.cells[37] = 1  # row 5, col 2 — red

        goal = ResetBoard.Goal()
        goal.final_board_state = board
        future = self.reset_client.send_goal_async(
            goal, feedback_callback=self._reset_feedback_cb
        )
        future.add_done_callback(self._reset_response_cb)

    def _reset_feedback_cb(self, fb_msg):
        self.get_logger().info('[TEST] ResetBoard feedback: %s' % fb_msg.feedback.status)

    def _reset_response_cb(self, future):
        gh = future.result()
        if not gh.accepted:
            self.get_logger().error('[TEST] ResetBoard goal rejected')
            self._finish()
            return
        self.get_logger().info('[TEST] ResetBoard goal accepted — waiting for result')
        gh.get_result_async().add_done_callback(self._reset_result_cb)

    def _reset_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            '[TEST] ResetBoard result: success=%s  msg="%s"' % (result.success, result.message)
        )
        self._finish()

    # ------------------------------------------------------------------ #

    def _finish(self):
        self.get_logger().info('=== Connect4 Action Tests DONE ===')


def main(args=None):
    rclpy.init(args=args)
    node = TestActionsNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
