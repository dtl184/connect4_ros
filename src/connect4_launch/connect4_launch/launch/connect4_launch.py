from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='connect4_perception',
            executable='board_perception_node',
            name='board_perception_node',
            output='screen'
        ),
        Node(
            package='connect4_game',
            executable='referee_node',
            name='referee_node',
            output='screen'
        ),
        Node(
            package='connect4_turtlebotnav',
            executable='block_delivery_node',
            name='block_delivery_node',
            output='screen'
        ),
        Node(
            package='connect4_manip',
            executable='arm_manip_node',
            name='arm_manip_node',
            output='screen'
        ),
    ])
