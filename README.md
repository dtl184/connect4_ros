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

## Assignment commit hashes

Initial Implementation: 022b0f3
