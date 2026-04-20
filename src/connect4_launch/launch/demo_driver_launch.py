from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="connect4_turtlebotnav",
            executable="block_delivery_node",
            output="screen",
        ),
        Node(
            package="connect4_manip",
            executable="arm_manip_node",
            output="screen",
        ),
        Node(
            package="connect4_game",
            executable="demo_driver_node",
            output="screen",
        ),
    ])