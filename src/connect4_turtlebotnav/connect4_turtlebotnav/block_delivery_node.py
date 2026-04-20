import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

from connect4_msgs.action import DeliverBlock


def yaw_to_quaternion(yaw: float):
    """Return (z, w) for a planar yaw-only quaternion."""
    return math.sin(yaw / 2.0), math.cos(yaw / 2.0)


# Delivery poses: (x, y, yaw) in map frame for each player
PLAYER_DELIVERY_POSES = {
    1: (1.0,  0.5, 0.0),
    2: (1.0, -0.5, 0.0),
}


class BlockDeliveryNode(Node):
    def __init__(self):
        super().__init__('block_delivery_node')

        cb_group = ReentrantCallbackGroup()

        self.deliver_block_server = ActionServer(
            self,
            DeliverBlock,
            '/connect4/deliver_block',
            self.execute_deliver_block,
            callback_group=cb_group,
        )

        self.navigator = BasicNavigator()
        self.nav2_ready = False

        self.get_logger().info('BlockDeliveryNode started')

    # Action server                                                        

    def execute_deliver_block(self, goal_handle):
        player = goal_handle.request.player
        self.get_logger().info('Received DeliverBlock goal for player %d' % player)

        if player not in PLAYER_DELIVERY_POSES:
            goal_handle.abort()
            result = DeliverBlock.Result()
            result.success = False
            result.message = 'Unknown player %d' % player
            return result

        goal_pose = self._make_pose(*PLAYER_DELIVERY_POSES[player])

        self.get_logger().info(
            'Navigating to player %d at (%.2f, %.2f)' % (
                player,
                goal_pose.pose.position.x,
                goal_pose.pose.position.y,
            )
        )

        self.navigator.goToPose(goal_pose)

        while not self.navigator.isTaskComplete():
            fb = self.navigator.getFeedback()
            if fb is not None:
                self.get_logger().info(
                    'Navigating to player %d...' % player, throttle_duration_sec=1.0
                )
            time.sleep(0.1)

        nav_result = self.navigator.getResult()
        result = DeliverBlock.Result()

        if nav_result == TaskResult.SUCCEEDED:
            goal_handle.succeed()
            result.success = True
            result.message = 'Delivered block to player %d' % player
            self.get_logger().info(result.message)
        else:
            goal_handle.abort()
            result.success = False
            result.message = 'Nav2 failed for player %d: %s' % (player, nav_result)
            self.get_logger().error(result.message)

        return result


    def _make_pose(self, x: float, y: float, yaw: float) -> PoseStamped:
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        
        qz, qw = yaw_to_quaternion(yaw)
        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw
        return pose


def main(args=None):
    rclpy.init(args=args)
    node = BlockDeliveryNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.add_node(node.navigator)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
