import time
from typing import List

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import PoseStamped
from shape_msgs.msg import SolidPrimitive

from moveit_msgs.action import MoveGroup
from moveit_msgs.msg import (
    BoundingVolume,
    Constraints,
    MoveItErrorCodes,
    OrientationConstraint,
    PositionConstraint,
)

from connect4_msgs.action import ResetBoard
from connect4_msgs.msg import BoardState


class ArmManipNode(Node):

    def __init__(self):
        super().__init__("arm_manip_node")

        self.cb_group = ReentrantCallbackGroup()

        self.reset_board_server = ActionServer(
            self,
            ResetBoard,
            "/connect4/reset_board",
            self.execute_reset_board,
            callback_group=self.cb_group,
        )

        self.move_group_client = ActionClient(
            self,
            MoveGroup,
            "/move_action",
            callback_group=self.cb_group,
        )

        self.move_group_name = "ur_manipulator"
        self.ee_link_name = "tool0"

        self.planning_frame = "base_link"

        # hard coded poses for now, will eventually get these from the camera
        self.home_pose = self.make_pose(0.35, 0.00, 0.35)
        self.pick_pose = self.make_pose(0.45, 0.12, 0.12)
        self.lift_pose = self.make_pose(0.45, 0.12, 0.22)
        self.drop_red_pose = self.make_pose(0.25, -0.22, 0.18)
        self.drop_blue_pose = self.make_pose(0.25, 0.22, 0.18)

        self.get_logger().info("ArmManipNode started")

    def make_pose(self, x: float, y: float, z: float) -> PoseStamped:
        pose = PoseStamped()
        pose.header.frame_id = self.planning_frame
        pose.header.stamp = self.get_clock().now().to_msg()

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        pose.pose.orientation.x = 1.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 0.0
        return pose

    def make_goal_constraints(self, target: PoseStamped) -> Constraints:
        c = Constraints()

        pc = PositionConstraint()
        pc.header = target.header
        pc.link_name = self.ee_link_name

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.01, 0.01, 0.01]

        region = BoundingVolume()
        region.primitives.append(box)
        region.primitive_poses.append(target.pose)

        pc.constraint_region = region
        pc.weight = 1.0

        oc = OrientationConstraint()
        oc.header = target.header
        oc.link_name = self.ee_link_name
        oc.orientation = target.pose.orientation
        oc.absolute_x_axis_tolerance = 0.2
        oc.absolute_y_axis_tolerance = 0.2
        oc.absolute_z_axis_tolerance = 0.2
        oc.weight = 1.0

        c.position_constraints.append(pc)
        c.orientation_constraints.append(oc)
        return c

    def move_to_pose(self, target: PoseStamped, label: str) -> bool:
        self.get_logger().info(
            f"Planning MoveIt motion to {label}: "
            f"x={target.pose.position.x:.3f}, "
            f"y={target.pose.position.y:.3f}, "
            f"z={target.pose.position.z:.3f}"
        )

        if not self.move_group_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error("MoveIt /move_action server not available")
            return False

        goal = MoveGroup.Goal()
        goal.request.group_name = self.move_group_name
        goal.request.num_planning_attempts = 5
        goal.request.allowed_planning_time = 5.0
        goal.request.max_velocity_scaling_factor = 0.2
        goal.request.max_acceleration_scaling_factor = 0.2
        goal.request.goal_constraints = [self.make_goal_constraints(target)]

        goal.planning_options.plan_only = False
        goal.planning_options.look_around = False
        goal.planning_options.replan = False

        send_future = self.move_group_client.send_goal_async(goal)

        while not send_future.done():
            time.sleep(0.05)

        goal_handle = send_future.result()
        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error(f"MoveIt goal to {label} was rejected")
            return False

        result_future = goal_handle.get_result_async()
        while not result_future.done():
            time.sleep(0.05)

        result = result_future.result().result
        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            self.get_logger().info(f"MoveIt motion to {label} succeeded")
            return True

        self.get_logger().error(
            f"MoveIt motion to {label} failed with code {result.error_code.val}"
        )
        return False

    def close_gripper(self) -> bool:
        self.get_logger().info("Closing gripper (demo stub)")
        time.sleep(1.0)
        return True

    def open_gripper(self) -> bool:
        self.get_logger().info("Opening gripper (demo stub)")
        time.sleep(1.0)
        return True

    def get_occupied_cells(self, board_state: BoardState) -> List[int]:
        occupied = [i for i, val in enumerate(board_state.cells) if val != 0]
        if not occupied:
            occupied = [35]
        return occupied

    def cell_to_pick_pose(self, cell_index: int) -> PoseStamped:
        rows, cols = 6, 7
        row = cell_index // cols
        col = cell_index % cols

        x0 = 0.42
        y0 = -0.09
        dx = 0.0
        dy = 0.03
        z = 0.11 + (5 - row) * 0.01

        return self.make_pose(x0 + dx, y0 + col * dy, z)

    def get_bin_pose(self, cell_value: int) -> PoseStamped:
        # 1 = red, 2 = blue, else default red
        if cell_value == 2:
            return self.drop_blue_pose
        return self.drop_red_pose

    def execute_reset_board(self, goal_handle):
        self.get_logger().info("Received ResetBoard goal")
        feedback = ResetBoard.Feedback()

        board_state = goal_handle.request.final_board_state
        occupied = self.get_occupied_cells(board_state)
        first_cell = occupied[0]
        first_value = 1
        if 0 <= first_cell < len(board_state.cells):
            first_value = board_state.cells[first_cell] if board_state.cells[first_cell] != 0 else 1

        self.pick_pose = self.cell_to_pick_pose(first_cell)
        drop_pose = self.get_bin_pose(first_value)

        ok = True

        feedback.status = "Moving home"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.move_to_pose(self.home_pose, "home")

        feedback.status = "Moving to pick pose"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.move_to_pose(self.pick_pose, "pick pose")

        feedback.status = "Closing gripper"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.close_gripper()

        feedback.status = "Lifting block"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.move_to_pose(self.lift_pose, "lift pose")

        feedback.status = "Moving to drop pose"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.move_to_pose(drop_pose, "drop pose")

        feedback.status = "Opening gripper"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.open_gripper()

        feedback.status = "Returning home"
        goal_handle.publish_feedback(feedback)
        ok = ok and self.move_to_pose(self.home_pose, "home")

        result = ResetBoard.Result()
        if ok:
            goal_handle.succeed()
            result.success = True
            result.message = "Reset sequence completed"
            self.get_logger().info(result.message)
        else:
            goal_handle.abort()
            result.success = False
            result.message = "Reset sequence failed"
            self.get_logger().error(result.message)

        return result


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


if __name__ == "__main__":
    main()