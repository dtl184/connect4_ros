from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    TimerAction,
    ExecuteProcess,
)
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    robot_ip = LaunchConfiguration("robot_ip")
    ur_type = LaunchConfiguration("ur_type")
    video_device = LaunchConfiguration("video_device")

    ur_driver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ur_robot_driver"),
                "launch",
                "ur_control.launch.py",
            ])
        ),
        launch_arguments={
            "ur_type": ur_type,
            "robot_ip": robot_ip,
            "launch_rviz": "false",
        }.items(),
    )

    moveit = ExecuteProcess(
        cmd=[
            "ros2",
            "launch",
            "ur_moveit_config",
            "ur_moveit.launch.py",
            "ur_type:=ur3e",
            "launch_rviz:=false",
        ],
        output="screen",
    )

    camera = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        name="camera",
        parameters=[
            {"video_device": video_device},
        ],
        output="screen",
    )

    block_detector = Node(
        package="connect4_perception",
        executable="block_pose_detector_node",
        name="block_detector",
        output="screen",
    )

    gripper_service = Node(
        package="connect4_manip",
        executable="robotiq_gripper_service",
        name="robotiq_gripper_service",
        output="screen",
    )

    reset_board_server = Node(
        package="connect4_manip",
        executable="reset_board_action_server",
        name="reset_board_server",
        output="screen",
    )

    pick_and_place_server = Node(
        package="connect4_manip",
        executable="pick_and_place_action_server",
        name="pick_and_place_server",
        output="screen",
    )

    pick_and_drop_server = Node(
        package="connect4_manip",
        executable="pick_and_drop_action_server",
        name="pick_and_drop_server",
        output="screen",
    )

    player = Node(
        package="connect4_game",
        executable="player",
        name="player",
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("robot_ip", default_value="192.168.1.2"),
        DeclareLaunchArgument("ur_type", default_value="ur3e"),
        DeclareLaunchArgument("video_device", default_value="/dev/video0"),

        TimerAction(period=0.0, actions=[
            camera,
            block_detector,
            ur_driver,
            gripper_service,
        ]),

        TimerAction(period=5.0, actions=[moveit]),

        TimerAction(period=10.0, actions=[
            reset_board_server,
            pick_and_place_server,
            pick_and_drop_server,
            player,
        ]),
    ])