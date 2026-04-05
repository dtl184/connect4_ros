import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient

from geometry_msgs.msg import PoseStamped
from connect4_msgs.action import DeliverBlock


class BlockDeliveryNode(Node):
    def __init__(self):
        super().__init__('block_delivery_node')

        self.deliver_block_server = ActionServer(
            self,
            DeliverBlock,
            '/connect4/deliver_block',
            self.execute_deliver_block
        )

        self.player_positions = {
            1: None,
            2: None,
            # todo: determine player poses
        }

    def execute_deliver_block(self, goal_handle):
        player = goal_handle.request.player

        if player in self.player_positions:
            target_pose = self.player_positions[player]

        goal_handle.succeed()
        result = DeliverBlock.Result()
        result.success = True
        result.message = f'Delivered block to player {player}'
        return result


def main(args=None):
    rclpy.init(args=args)
    node = BlockDeliveryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
