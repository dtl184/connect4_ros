# ROS2 Game Referee 

This project implements a robotic Tic-Tac-Toe referee system using ROS2.  

## Packages

connect4_msgs  
Custom messages and actions:
- BoardState.msg
- Winner.msg
- DeliverBlock.action
- ResetBoard.action

connect4_perception  
Board perception node using camera input.

connect4_game  
Referee node implementing game logic.

connect4_turtlebotnav  
Turtlebot block delivery action server.

connect4_manip  
UR3 manipulation node for resetting the board.

connect4_launch  
Launch file for full system.

## External Dependencies

- ROS2
- Nav2
- MoveIt2
- OpenCV
- UR3 driver
- Turtlebot packages

## Assignments

Here is where you will find the parts of my project that correspond to the class assignments

Initial Implementation: 022b0f3 (commit hash)

MoveIt:

`connect4_manip/connect4_manip/pick_and_place_server.py`
       
`connect4_manip/connect4_manip/pick_and_drop_server.py`

Nav2: `connect4_turtlebotnav/connect4_turtlebotnav/turtle_deliver_server.py`

Perception: `connect4_perception/connect4_perception/block_pose_detector_node.py`

High-Level control: 

`connect4_game/connect4_game/tic_tac_toe_referee.py`

`connect4_game/connect4_game/tic_tac_toe_player.py` (custom, handwritten node)

## How to run
1. Turn on the ur3e arm using the Teach Pendant.
2. Create a custom program on the Teach Pendant with an External Control node.
3. Connect ur3e control box to computer running ROS system with ethernet.
4. Enter the following into a terminal on the ROS computer:
   
   `cd ~/connect4_ros`
   
   `source /opt/ros/kilted/setup.bash`
   
   `source install/setup.bash`
   
5. Start either referee mode or player mode.
   
   `ros2 launch connect4_launch referee.launch.py video_device:=/dev/video0`
   
   `ros2 launch connect4_launch player.launch.py video_device:=/dev/video0`
   
   Replace `/dev/video0` with whatever your camera is.
   
7. Once all ROS nodes have launched, press play on the Teach Pendant.

# Note on Nav2

The Nav2 component of my project currently only works in simulation. Additionally, I discovered there are problems when Nav2 and MoveIt are run with same ROS_DOMAIN_ID. I attempted to solve this by using Python Flask to create an http server so my Nav2 nodes could still communicate with my other ROS nodes with a different domain ID, but I was unable to make this work. 

Instead, my video shows me manually starting Nav2 and sending a command, to simulate what the Turtlebot should do after the board is reset. To recreate this, run the following commands.

1. In one terminal, run the following to launch Rviz, Gazebo, and the turtlebot action server. When Rviz opens, indicate the robot's initial pose on the map.

`ros2 launch connect4_launch turtle.launch.py`

2. In another, run this command to see the Turtlebot move in Gazebo.

`ros2 action send_goal /connect4/turtle_deliver connect4_msgs/action/TurtleDeliver "{x: 1.0, y: 0.0, yaw: 0.0}"`

