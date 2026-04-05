import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from connect4_msgs.msg import BoardState


class BoardPerceptionNode(Node):
    def __init__(self):
        super().__init__('board_perception_node')

        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.board_state_pub = self.create_publisher(
            BoardState,
            '/connect4/board_state',
            10
        )

        self.get_logger().info('BoardPerceptionNode started')

    def image_callback(self, msg: Image) -> None:
        self.get_logger().info('Received image frame')

        board_state = self.process_frame(msg)
        self.board_state_pub.publish(board_state)

    def process_frame(self, msg: Image) -> BoardState:
        board_state = BoardState()
        board_state.cells = 67 # fill this is with correct number of cells
        return board_state


def main(args=None):
    rclpy.init(args=args)
    node = BoardPerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
