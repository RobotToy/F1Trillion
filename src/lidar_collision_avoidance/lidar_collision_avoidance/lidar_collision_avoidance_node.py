import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LidarObstacleDetectionNode(Node):
    def __init__(self):
        super().__init__('lidar_obstacle_detection_node')

        # Publisher for /cmd_vel to send motion commands
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscriber for LiDAR scan data
        self.lidar_sub = self.create_subscription(
            LaserScan,
            '/scan',  # LiDAR topic name (adjust based on your setup)
            self.lidar_callback,
            10
        )

        # Obstacle detection state
        self.obstacle_distance_threshold = 0.3048  # 1 foot in meters
        self.angle_range = 10  # Degrees left and right from the front of the car
        self.obstacle_detected = False  # Initially, no obstacle is detected

    def lidar_callback(self, msg):
        # Determine the index range for the front +/- 10 degrees
        # Assuming LiDAR scan data covers 0 to 359 degrees
        # Example: If the middle index is 180 (facing front), range is 170 to 190
        total_angles = len(msg.ranges)
        front_index = total_angles // 2  # Index of the front (0 degrees)
        start_index = max(front_index - self.angle_range, 0)
        end_index = min(front_index + self.angle_range, total_angles - 1)

        # Filter out invalid ranges (inf or NaN) in the specified angle range
        valid_ranges = [distance for distance in msg.ranges[start_index:end_index + 1] 
                        if not (float('inf') == distance or float('nan') == distance)]

        # Check if any valid range in the specified angle range is below the threshold
        if any(distance < self.obstacle_distance_threshold for distance in valid_ranges):
            if not self.obstacle_detected:  # Check to avoid redundant stop commands
                self.obstacle_detected = True
                self.get_logger().info("Obstacle detected within 1 foot in front: Stopping the car.")
                self.send_stop_command()
        else:
            if self.obstacle_detected:  # Clear obstacle status if it was previously detected
                self.get_logger().info("Obstacle cleared: Resuming forward motion.")
            self.obstacle_detected = False
            self.send_move_forward_command()

    def send_stop_command(self):
        # Create a Twist message with zero velocity to stop the car
        cmd_vel = Twist()
        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd_vel)

    def send_move_forward_command(self):
        # Create a Twist message with forward velocity
        cmd_vel = Twist()
        cmd_vel.linear.x = 0.2  # Forward speed (adjust as needed)
        cmd_vel.angular.z = -0.5
        self.cmd_vel_pub.publish(cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    node = LidarObstacleDetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()





