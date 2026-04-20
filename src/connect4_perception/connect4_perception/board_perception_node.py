import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image
from connect4_msgs.msg import BoardState

try:
    import cv2
    import numpy as np
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

BOARD_ROWS = 6
BOARD_COLS = 7
PROCESS_RATE_HZ = 2.0   


class BoardPerceptionNode(Node):
    def __init__(self):
        super().__init__('board_perception_node')

        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            qos_profile_sensor_data,
        )

        self.board_state_pub = self.create_publisher(
            BoardState,
            '/connect4/board_state',
            10,
        )

        self._last_process_time = self.get_clock().now()
        self._min_interval_ns = int(1e9 / PROCESS_RATE_HZ)

        self.get_logger().info('BoardPerceptionNode started')

    def image_callback(self, msg: Image) -> None:
        now = self.get_clock().now()
        elapsed_ns = (now - self._last_process_time).nanoseconds
        if elapsed_ns < self._min_interval_ns:
            return
        self._last_process_time = now

        board_state = self.process_frame(msg)
        self.board_state_pub.publish(board_state)

    def process_frame(self, msg: Image) -> BoardState:
        board_state = BoardState()

        if not CV2_AVAILABLE:
            board_state.cells = [0] * (BOARD_ROWS * BOARD_COLS)
            return board_state

        # Convert ROS Image to OpenCV BGR
        frame = self._ros_image_to_cv2(msg)
        if frame is None:
            board_state.cells = [0] * (BOARD_ROWS * BOARD_COLS)
            return board_state

        cells = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                cells.append(self._detect_cell_color(frame, row, col))

        board_state.cells = cells
        return board_state

    def _ros_image_to_cv2(self, msg: Image):
        """Convert a sensor_msgs/Image (BGR8 or RGB8) to a NumPy array."""
        try:
            dtype = np.uint8
            frame = np.frombuffer(msg.data, dtype=dtype).reshape(
                msg.height, msg.width, -1
            )
            if msg.encoding == 'rgb8':
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            return frame
        except Exception as e:
            self.get_logger().error('Image conversion failed: %s' % str(e))
            return None

    def _detect_cell_color(self, frame, row: int, col: int) -> int:
        """Return 0 (empty), 1 (red), or 2 (blue) for a board cell.

        Divides the frame into a BOARD_ROWS x BOARD_COLS grid and checks the
        dominant HSV color in each cell region.
        """
        h, w = frame.shape[:2]
        cell_h = h // BOARD_ROWS
        cell_w = w // BOARD_COLS

        y1, y2 = row * cell_h, (row + 1) * cell_h
        x1, x2 = col * cell_w, (col + 1) * cell_w
        roi = frame[y1:y2, x1:x2]

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Red spans two hue ranges in HSV
        red_mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
        red_mask |= cv2.inRange(hsv, (160, 100, 100), (180, 255, 255))
        blue_mask = cv2.inRange(hsv, (100, 100, 100), (130, 255, 255))

        red_px = int(cv2.countNonZero(red_mask))
        blue_px = int(cv2.countNonZero(blue_mask))
        total_px = roi.shape[0] * roi.shape[1]
        threshold = int(total_px * 0.25)

        if red_px > threshold and red_px >= blue_px:
            return 1
        if blue_px > threshold:
            return 2
        return 0


def main(args=None):
    rclpy.init(args=args)
    node = BoardPerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
