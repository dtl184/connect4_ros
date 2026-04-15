import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose
from connect4_msgs.action import ResetBoard
from connect4_msgs.msg import BoardState
import time

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

        self.gripper_pub = self.create_publisher(Float64, "/gripper/command", 10)

        self.GRIPPER_OPEN = 0.0
        self.GRIPPER_CLOSED = 0.8   # TODO: tune this

    def execute_reset_board(self, goal_handle):
        final_board_state = goal_handle.request.final_board_state
        occupied_cells = self.get_occupied_cells(final_board_state)

        for cell_index, piece_color in occupied_cells:
            pick_pose = self.cell_to_pick_pose(cell_index)
            pick_approach = self.offset_pose_z(pick_pose, self.approach_z)

            place_pose = self.get_bin_pose(piece_color)
            place_approach = self.offset_pose_z(place_pose, self.approach_z)

            if not self.move_to_pose(pick_approach, self.board_frame):
                return self.fail_result(goal_handle, "Failed moving to pick approach")

            if not self.move_to_pose(pick_pose, self.board_frame):
                return self.fail_result(goal_handle, "Failed moving to pick pose")

            self.grasp_block()

            if not self.move_to_pose(pick_approach, self.board_frame):
                return self.fail_result(goal_handle, "Failed lifting from board")

            if not self.move_to_pose(place_approach, self.base_frame):
                return self.fail_result(goal_handle, "Failed moving to place approach")

            if not self.move_to_pose(place_pose, self.base_frame):
                return self.fail_result(goal_handle, "Failed moving to place pose")

            self.place_block()

            if not self.move_to_pose(place_approach, self.base_frame):
                return self.fail_result(goal_handle, "Failed retreating from bin")

        goal_handle.succeed()
        result = ResetBoard.Result()
        result.success = True
        result.message = "Reset complete"
        return result

    def get_occupied_cells(self, board_state: BoardState):
        occupied = []
        for idx, value in enumerate(board_state.cells):
            if value != 0:
                occupied.append((idx, value))
        return occupied
    
    def offset_pose_z(self, pose: Pose, dz: float) -> Pose:
        p = Pose()
        p.position.x = pose.position.x
        p.position.y = pose.position.y
        p.position.z = pose.position.z + dz
        p.orientation = pose.orientation
        return p
    
    def cell_to_row_col(self, cell_index: int):
        row = cell_index // self.cols
        col = cell_index % self.cols
        return row, col

    def cell_to_pick_pose(self, cell_index: int) -> Pose:
        row, col = self.cell_to_row_col(cell_index)

        pose = Pose()
        pose.position.x = self.board_origin_x + col * self.cell_dx
        pose.position.y = self.board_origin_y + row * self.cell_dy
        pose.position.z = self.pick_z

        pose.orientation.x = 0.0
        pose.orientation.y = 1.0
        pose.orientation.z = 0.0
        pose.orientation.w = 0.0
        return pose

    def get_bin_pose(self, piece_color: int) -> Pose:
        if piece_color == 1:
            return self.blue_bin_pose
        elif piece_color == 2:
            return self.red_bin_pose
        else:
            raise ValueError(f"Unknown piece color: {piece_color}")
        
    def move_to_pose(self, pose: Pose, frame_id: str = None) -> bool:
        if frame_id is None:
            frame_id = self.base_frame

        self.arm.set_start_state_to_current_state()
        self.arm.set_goal_state(pose_stamped_msg=(frame_id, pose))

        plan_result = self.arm.plan()
        if not plan_result:
            self.get_logger().error("Planning failed")
            return False

        # execute API details depend on your exact moveit_py version/config
        self.moveit.execute(plan_result.trajectory, controllers=[])
        return True

    def grasp_block(self):
        msg = Float64()
        msg.data = self.GRIPPER_CLOSED
        self.gripper_pub.publish(msg)

        time.sleep(1.0)

    def lift_block(self, current_pose: Pose):
        lift_pose = self.offset_pose_z(current_pose, self.approach_z)

        return self.move_to_pose(lift_pose, self.board_frame)

    def place_block(self):
        msg = Float64()
        msg.data = self.GRIPPER_OPEN
        self.gripper_pub.publish(msg)

        time.sleep(1.0)


def main(args=None):
    rclpy.init(args=args)
    node = ArmManipNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
