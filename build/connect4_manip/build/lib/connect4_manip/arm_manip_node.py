import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from geometry_msgs.msg import Pose
from connect4_msgs.action import ResetBoard
from connect4_msgs.msg import BoardState


class ArmManipNode(Node):
    def __init__(self):
        super().__init__('arm_manip_node')

        self.reset_board_server = ActionServer(
            self,
            ResetBoard,
            '/connect4/reset_board',
            self.execute_reset_board
        )

        self.get_logger().info('ArmManipNode started')

    def execute_reset_board(self, goal_handle):
        """ResetBoard action callback."""
        final_board_state = goal_handle.request.final_board_state

        occupied_cells = self.get_occupied_cells(final_board_state)
        # just loop through all cells instead of planning
        for cell_index, piece_color in occupied_cells:
            pick_pose = self.cell_to_pick_pose(cell_index)
            place_pose = self.get_bin_pose(piece_color)

            self.move_to_pose(pick_pose)
            self.grasp_block()
            self.lift_block()
            self.move_to_pose(place_pose)
            self.place_block()

        goal_handle.succeed()

        result = ResetBoard.Result()
        result.success = True
        result.message = "Reset complete"
        return result

    def get_occupied_cells(self, board_state: BoardState):
        # return list of occupied cells
        pass

    def cell_to_pick_pose(self, cell_index: int) -> Pose:
        # convert board cell to pick pose
        pass

    def get_bin_pose(self, piece_color: int) -> Pose:
        # return bin pose for piece color 
        pass

    def move_to_pose(self, pose: Pose):
        # move arm to pose using MoveIt 
        pass

    def grasp_block(self):
        # close gripper on block 
        pass

    def lift_block(self):
        # lift block after grasp
        pass

    def place_block(self):
        # open gripper to place block
        pass


def main(args=None):
    rclpy.init(args=args)
    node = ArmManipNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
