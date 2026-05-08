from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


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

    moveit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ur_moveit_config"),
                "launch",
                "ur_moveit.launch.py",
            ])
        ),
        launch_arguments={
            "ur_type": ur_type,
            "launch_rviz": "false",
        }.items(),
    )

    camera = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        name="camera",
        parameters=[
            {"video_device": video_device},
        ],
    )

    block_detector = Node(
        package="connect4_perception",
        executable="block_detector_node",
        name="block_detector",
        output="screen",
    )

    reset_board_server = Node(
        package="connect4_manip",
        executable="reset_board_server",
        name="reset_board_server",
        output="screen",
    )

    player = Node(
        package="connect4_game",
        executable="player",
        name="player",
        output="screen",
    )

    pick_and_place_server = Node(
        package="connect4_manip",
        executable="pick_and_place_server",
        name="pick_and_place_server",
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("robot_ip", default_value="192.168.1.2"),
        DeclareLaunchArgument("ur_type", default_value="ur3e"),
        DeclareLaunchArgument("video_device", default_value="/dev/video0"),

        camera,
        block_detector,

        ur_driver,

        TimerAction(period=5.0, actions=[moveit]),

        TimerAction(period=8.0, actions=[
            reset_board_server,
            pick_and_place_server,
            player,
        ]),
    ])