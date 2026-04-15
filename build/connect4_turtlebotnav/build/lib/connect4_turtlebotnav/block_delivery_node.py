import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
from connect4_msgs.action import DeliverBlock
import time


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

    def navigate_to_pose(self, pose: PoseStamped) -> bool:
        if not self.nav_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error('Nav2 server not available')
            return False

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        future = self.nav_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, future)

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Navigation goal rejected')
            return False

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result().result

        return result
    
    def execute_deliver_block(self, goal_handle):
        player = goal_handle.request.player
        self.get_logger().info(f'Received request to deliver to player {player}')

        if player not in self.player_positions:
            goal_handle.abort()
            result = DeliverBlock.Result()
            result.success = False
            result.message = f'Unknown player {player}'
            return result

        target_pose = self.player_positions[player]

        success = self.navigate_to_pose(target_pose)

        if not success:
            goal_handle.abort()
            result = DeliverBlock.Result()
            result.success = False
            result.message = 'Navigation failed'
            return result

        # wait for human to take block
        time.sleep(2.0)

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
