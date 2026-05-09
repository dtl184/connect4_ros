from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    TimerAction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    set_tb3_model = SetEnvironmentVariable(
        name="TURTLEBOT3_MODEL",
        value="waffle",
    )

    nav2_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("nav2_bringup"),
                "launch",
                "tb3_simulation_launch.py",
            ])
        ),
        launch_arguments={
            "headless": "False",
            "autostart": "True",
            "use_rviz": "True",
            "rviz_config_file": PathJoinSubstitution([
                FindPackageShare("nav2_bringup"),
                "rviz",
                "nav2_default_view.rviz",
            ]),
        }.items(),
    )

    turtle_deliver_server = Node(
        package="connect4_turtlebotnav",
        executable="turtle_deliver_server",
        name="turtle_deliver_server",
        output="screen",
    )

    return LaunchDescription([
        set_tb3_model,

        nav2_sim,

        TimerAction(
            period=8.0,
            actions=[turtle_deliver_server],
        ),
    ])