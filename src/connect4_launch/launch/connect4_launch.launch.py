# connect4_launch.launch.py
#
# Launches the full Connect-4 Referee system including Nav2 (for TurtleBot
# navigation) and MoveIt! move_group (for UR3 arm control).
#
# Prerequisites — install and source before running:
#   sudo apt install ros-$ROS_DISTRO-nav2-bringup
#   sudo apt install ros-$ROS_DISTRO-ur-moveit-config
#   sudo apt install ros-$ROS_DISTRO-ur-robot-driver
#
# For simulation add one of:
#   ros-$ROS_DISTRO-turtlebot3-gazebo   (TurtleBot3)
#   ros-$ROS_DISTRO-ur-simulation-gazebo (UR3 Gazebo)
#
# Launch:
#   ros2 launch connect4_launch connect4_launch.launch.py
#   ros2 launch connect4_launch connect4_launch.launch.py use_sim_time:=false

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    # ------------------------------------------------------------------ #
    # Nav2 — navigation stack for the TurtleBot block-delivery robot      #
    # ------------------------------------------------------------------ #
    nav2_dir = get_package_share_directory('nav2_bringup')
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
            # Supply a robot-specific params file when running on hardware:
            # 'params_file': '/path/to/nav2_params.yaml',
        }.items(),
    )

    # ------------------------------------------------------------------ #
    # MoveIt! — move_group node for the UR3 arm                           #
    # ------------------------------------------------------------------ #
    # Requires ur_moveit_config (or equivalent) to be installed.
    # The launch file below starts move_group with UR3 kinematics and
    # controller configuration.  Replace with your robot-specific config
    # if using a different arm.
    ur_moveit_dir = get_package_share_directory('ur_moveit_config')
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ur_moveit_dir, 'launch', 'ur_moveit.launch.py')
        ),
        launch_arguments={
            'ur_type': 'ur3',
            'use_sim_time': use_sim_time,
            'launch_rviz': 'false',
        }.items(),
    )

    # ------------------------------------------------------------------ #
    # Custom Connect-4 nodes                                               #
    # ------------------------------------------------------------------ #
    node_params = [{'use_sim_time': use_sim_time}]

    perception_node = Node(
        package='connect4_perception',
        executable='board_perception_node',
        name='board_perception_node',
        output='screen',
        parameters=node_params,
    )

    referee_node = Node(
        package='connect4_game',
        executable='referee_node',
        name='referee_node',
        output='screen',
        parameters=node_params,
    )

    block_delivery_node = Node(
        package='connect4_turtlebotnav',
        executable='block_delivery_node',
        name='block_delivery_node',
        output='screen',
        parameters=node_params,
    )

    arm_manip_node = Node(
        package='connect4_manip',
        executable='arm_manip_node',
        name='arm_manip_node',
        output='screen',
        parameters=node_params,
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation clock (true for Gazebo, false for hardware)',
        ),
        nav2_launch,
        moveit_launch,
        perception_node,
        referee_node,
        block_delivery_node,
        arm_manip_node,
    ])
