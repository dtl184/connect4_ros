# ROS2 Connect4 Referee 

This project implements a robotic Connect Four referee system using ROS2.  
Two players place blocks on a flat Connect4 board. A Turtlebot delivers blocks,
a perception node detects board state, a referee node manages game logic, and
a UR3 arm resets the board after a win.

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

MoveIt: connect4_manip/connect4_manip/pick_and_place_server.py
        connect4_manip/connect4_manip/pick_and_drop_server.py

Nav2: connect4_turtlebotnav/connect4_turtlebotnav/turtle_deliver_server.py

Perception: connect4_perception/connect4_perception/block_pose_detector_node.py

High-Level control: connect4_game/connect4_game/tic_tac_toe_referee.py
                    connect4_game/connect4_game/tic_tac_toe_player.py (custom, handwritten node)

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
