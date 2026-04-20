# connect4_test.launch.py
#
# Minimal launch file for testing the Connect-4 action servers without
# requiring a live robot or full Nav2 / MoveIt stack.
#
# Launches:
#   - block_delivery_node  (DeliverBlock action server — Nav2 in stub/sim mode)
#   - arm_manip_node       (ResetBoard action server — MoveIt in stub mode)
#   - test_actions_node    (sends test goals to both servers and logs results)
#
# Run:
#   colcon build --packages-select connect4_msgs connect4_game connect4_manip \
#                                   connect4_turtlebotnav connect4_launch
#   source install/setup.bash
#   ros2 launch connect4_launch connect4_test.launch.py

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
