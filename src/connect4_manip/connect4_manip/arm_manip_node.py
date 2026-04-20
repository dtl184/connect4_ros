import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Pose, PoseStamped
from connect4_msgs.action import ResetBoard
from connect4_msgs.msg import BoardState

from moveit.planning import MoveItPy


try:
    from control_msgs.action import GripperCommand
    GRIPPER_AVAILABLE = True
except ImportError:
    GRIPPER_AVAILABLE = False


BOARD_ROWS = 6
BOARD_COLS = 7
CELL_SIZE = 0.05        # meters per cell

# Board top-left cell center in base_link frame
BOARD_ORIGIN_X = 0.30
BOARD_ORIGIN_Y = -0.15
BOARD_Z = 0.025         # block center height above table

APPROACH_Z = 0.12       # pre-pick hover height offset above block
LIFT_Z = 0.15           # post-grasp lift height offset

# Place-pose (x, y, z) for each piece color
BIN_POSES = {
    1: (0.00,  0.45, 0.05),   # red bin
    2: (0.00, -0.45, 0.05),   # blue bin
}

ARM_GROUP = 'manipulator'
EEF_LINK = 'tool0'
BASE_FRAME = 'base_link'
GRIPPER_ACTION = '/gripper_controller/gripper_cmd'
GRIPPER_OPEN = 0.08
GRIPPER_CLOSED = 0.005
GRIPPER_MAX_EFFORT = 50.0


class ArmManipNode(Node):
    def __init__(self):
        super().__init__('arm_manip_node')

        cb_group = ReentrantCallbackGroup()

        self.reset_board_server = ActionServer(
            self,
            ResetBoard,
            '/connect4/reset_board',
            self.execute_reset_board,
            callback_group=cb_group,
        )

        self.moveit = MoveItPy(node_name='arm_manip_moveit')
        self.arm = self.moveit.get_planning_component(ARM_GROUP)
        self.get_logger().info('MoveItPy initialized with group "%s"' % ARM_GROUP)

        self.gripper_client = ActionClient(
            self, GripperCommand, GRIPPER_ACTION, callback_group=cb_group
        )

        self.get_logger().info('ArmManipNode started')

    # Action server                                                        

    def execute_reset_board(self, goal_handle):
        self.get_logger().info('Executing ResetBoard action')
        board = goal_handle.request.final_board_state
        occupied = self.get_occupied_cells(board)
        self.get_logger().info('Clearing %d blocks' % len(occupied))

        for i, (cell_idx, color) in enumerate(occupied):
            fb = ResetBoard.Feedback()
            fb.status = 'Clearing cell %d (%d/%d)' % (cell_idx, i + 1, len(occupied))
            goal_handle.publish_feedback(fb)
            self.get_logger().info(fb.status)

            pick_pose = self.cell_to_pick_pose(cell_idx)
            place_pose = self.get_bin_pose(color)

            self.move_to_approach(pick_pose)
            self.move_to_pose(pick_pose)
            self.grasp_block()
            self.lift_block(pick_pose)
            self.move_to_pose(place_pose)
            self.place_block()

        goal_handle.succeed()
        result = ResetBoard.Result()
        result.success = True
        result.message = 'Cleared %d blocks' % len(occupied)
        self.get_logger().info(result.message)
        return result

    def get_occupied_cells(self, board_state: BoardState):
        return [(i, v) for i, v in enumerate(board_state.cells) if v != 0]

    def cell_to_pick_pose(self, cell_index: int) -> Pose:
        col = cell_index % BOARD_COLS
        row = cell_index // BOARD_COLS
        pose = Pose()
        pose.position.x = BOARD_ORIGIN_X + col * CELL_SIZE
        pose.position.y = BOARD_ORIGIN_Y + row * CELL_SIZE
        pose.position.z = BOARD_Z
        pose.orientation.x = 1.0
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 0.0
        return pose

    def get_bin_pose(self, piece_color: int) -> Pose:
        x, y, z = BIN_POSES.get(piece_color, BIN_POSES[1])
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose.orientation.x = 1.0
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 0.0
        return pose



    def move_to_approach(self, target_pose: Pose):
        """Move to a hover point directly above the target before descending."""
        approach = Pose()
        approach.position.x = target_pose.position.x
        approach.position.y = target_pose.position.y
        approach.position.z = target_pose.position.z + APPROACH_Z
        approach.orientation = target_pose.orientation
        self.move_to_pose(approach)

    def move_to_pose(self, pose: Pose):
        """Plan and execute a Cartesian motion to pose via MoveIt!."""

        ps = PoseStamped()
        ps.header.frame_id = BASE_FRAME
        ps.header.stamp = self.get_clock().now().to_msg()
        ps.pose = pose

        self.arm.set_start_state_to_current_state()
        self.arm.set_goal_state(pose_stamped_msg=ps, pose_link=EEF_LINK)

        plan_result = self.arm.plan()
        if plan_result:
            self.get_logger().info('Plan found — executing trajectory')
            self.moveit.execute(plan_result.trajectory, blocking=True, controllers=[])
        else:
            self.get_logger().error('MoveIt! planning failed')

    def grasp_block(self):
        self.get_logger().info('Closing gripper to grasp block')
        self._send_gripper_goal(GRIPPER_CLOSED)

    def lift_block(self, current_pose: Pose):
        """Move straight up after grasping to clear the board surface."""
        lifted = Pose()
        lifted.position.x = current_pose.position.x
        lifted.position.y = current_pose.position.y
        lifted.position.z = current_pose.position.z + LIFT_Z
        lifted.orientation = current_pose.orientation
        self.move_to_pose(lifted)

    def place_block(self):
        self.get_logger().info('Opening gripper to place block')
        self._send_gripper_goal(GRIPPER_OPEN)

    def _send_gripper_goal(self, position: float):
        if self.gripper_client is None:
            self.get_logger().info('[STUB] gripper -> %.3f m' % position)
            return

        if not self.gripper_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().warn('Gripper action server not available')
            return

        goal = GripperCommand.Goal()
        goal.command.position = position
        goal.command.max_effort = GRIPPER_MAX_EFFORT

        send_future = self.gripper_client.send_goal_async(goal)
        while not send_future.done():
            time.sleep(0.02)

        gh = send_future.result()
        if not gh.accepted:
            self.get_logger().error('Gripper goal rejected')
            return

        result_future = gh.get_result_async()
        while not result_future.done():
            time.sleep(0.02)

        self.get_logger().info('Gripper moved to %.3f m' % position)


def main(args=None):
    rclpy.init(args=args)
    node = ArmManipNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
