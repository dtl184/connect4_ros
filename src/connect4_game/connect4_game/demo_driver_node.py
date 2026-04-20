import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from connect4_msgs.msg import BoardState
from connect4_msgs.action import DeliverBlock, ResetBoard


class DemoDriverNode(Node):
    """
    Dedicated assignment demo node:
    1. sends DeliverBlock(player=1)
    2. when that succeeds, sends ResetBoard(fake board)
    """

    def __init__(self):
        super().__init__("demo_driver_node")

        cb_group = ReentrantCallbackGroup()

        self.deliver_block_client = ActionClient(
            self,
            DeliverBlock,
            "/connect4/deliver_block",
            callback_group=cb_group,
        )

        self.reset_board_client = ActionClient(
            self,
            ResetBoard,
            "/connect4/reset_board",
            callback_group=cb_group,
        )

        self.started = False
        self.start_timer = self.create_timer(3.0, self.start_demo, callback_group=cb_group)
        self.get_logger().info("DemoDriverNode started")

    def start_demo(self):
        if self.started:
            return
        self.started = True
        self.start_timer.cancel()
        self.get_logger().info("Starting demo: deliver block to player 1")
        self.send_deliver_goal(1)

    def send_deliver_goal(self, player: int):
        if not self.deliver_block_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error("DeliverBlock server not available")
            return

        goal = DeliverBlock.Goal()
        goal.player = player

        future = self.deliver_block_client.send_goal_async(goal)
        future.add_done_callback(self._deliver_goal_response_cb)

    def _deliver_goal_response_cb(self, future):
        goal_handle = future.result()
        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("DeliverBlock goal rejected")
            return

        self.get_logger().info("DeliverBlock goal accepted")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._deliver_result_cb)

    def _deliver_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            f"DeliverBlock result: success={result.success}, msg={result.message}"
        )

        if not result.success:
            return

        self.get_logger().info("Now sending ResetBoard goal")
        self.send_reset_goal()

    def send_reset_goal(self):
        if not self.reset_board_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error("ResetBoard server not available")
            return

        goal = ResetBoard.Goal()

        # Fake board: one occupied cell so the arm has something to “reset”
        board = BoardState()
        board.cells = [0] * 42
        board.cells[35] = 1
        goal.final_board_state = board

        future = self.reset_board_client.send_goal_async(goal)
        future.add_done_callback(self._reset_goal_response_cb)

    def _reset_goal_response_cb(self, future):
        goal_handle = future.result()
        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("ResetBoard goal rejected")
            return

        self.get_logger().info("ResetBoard goal accepted")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._reset_result_cb)

    def _reset_result_cb(self, future):
        result = future.result().result
        self.get_logger().info(
            f"ResetBoard result: success={result.success}, msg={result.message}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = DemoDriverNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()