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

        self.get_logger().info('RefereeNode started')

    def board_state_callback(self, msg: BoardState) -> None:
        self.get_logger().info('Received board state')

        if self.is_winner(msg):
            winner_msg = Winner()
            winner_msg.winner = self.current_player
            self.winner_pub.publish(winner_msg)
            self.send_reset_board_goal(msg)
        else:
            self.send_deliver_block_goal(self.current_player)

    def is_winner(self, board_state: BoardState) -> bool:
        return False

    def is_legal_move(self, previous: BoardState, current: BoardState) -> bool:
        return True

    def send_deliver_block_goal(self, player: int) -> None:
        self.get_logger().info(f'Sending DeliverBlock goal for player {player}')
        goal_msg = DeliverBlock.Goal()
        goal_msg.player = player
        # todo: extend this skeleton

    def send_reset_board_goal(self, board_state: BoardState) -> None:
        self.get_logger().info('Sending ResetBoard goal')
        goal_msg = ResetBoard.Goal()
        goal_msg.final_board_state = board_state
        # todo: extend this skeleton


def main(args=None):
    rclpy.init(args=args)
    node = RefereeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
