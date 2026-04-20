# connect4_test.launch.py
# Launch file specifically for system testing purposes without a real robot

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    block_delivery_node = Node(
        package='connect4_turtlebotnav',
        executable='block_delivery_node',
        name='block_delivery_node',
        output='screen',
    )

    arm_manip_node = Node(
        package='connect4_manip',
        executable='arm_manip_node',
        name='arm_manip_node',
        output='screen',
    )

    test_actions_node = Node(
        package='connect4_game',
        executable='test_actions_node',
        name='test_actions_node',
        output='screen',
    )

    return LaunchDescription([
        block_delivery_node,
        arm_manip_node,
        test_actions_node,
    ])
