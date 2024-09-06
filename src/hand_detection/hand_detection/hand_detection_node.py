import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
import numpy as np
from roboflowoak import RoboflowOak
from cv_bridge import CvBridge, CvBridgeError
import time

class hand_detection_node(Node):
    def __init__(self):
        super().__init__('hand_dectection_node')

        # Initialize RoboflowOak
        self.rf = RoboflowOak(
            model="rock-paper-scissors-sxsw",
            confidence=0.05,
            overlap=0.5,
            version="14",
            api_key="kDi4xMfGMvnsVqisDYa1",
            rgb=True,
            depth=True,
            device=None,
            blocking=True
        )

        # Publisher for /cmd_vel
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Timer to call the callback function periodically
        self.timer = self.create_timer(1.0, self.timer_callback)  # Adjust the interval as needed

        # State Tracking
        self.moving = False  # Start the car in a stationary position
        self.last_rock_time = 0 
        self.move_duration = 3.0  # Time after starting until it will accept another command

        # Initialize OpenCV bridge
        self.bridge = CvBridge()

    def timer_callback(self):
        try:
            # Run model inference
            result, frame, raw_frame, depth = self.rf.detect()

            # Ensure depth and frame are valid
            if frame is None or depth is None:
                self.get_logger().warn("No frame or depth data received.")
                return

            predictions = result.get("predictions", [])

            # Extract class data from predictions
            class_data = [p.class_name for p in predictions]
            self.get_logger().info(f"Class Data: {class_data}")

            # Determine motion commands based on class data
            cmd_vel = Twist()

            # Get current time
            current_time = time.time()

            # Moving Criteria
            if "Rock" in class_data:
                if not self.moving:
                    # Start moving and record the time
                    self.moving = True
                    self.last_rock_time = current_time
                    self.get_logger().info("Rock detected: Starting to move forward")

            # Moving logic
            if self.moving:
                if current_time - self.last_rock_time <= self.move_duration:
                    # Continue moving forward till the duration after the first "Rock" has passed
                    cmd_vel.linear.x = 0.2
                    cmd_vel.angular.z = -0.5  # Go straight
                else:
                    # Continue moving for the duration after the first "rock"
                    cmd_vel.linear.x = 0.2
                    if "Scissors" in class_data:
                        cmd_vel.angular.z = -0.8  # Turn left on scissors
                        self.get_logger().info("Scissors detected: Turning Left")
                    elif "Paper" in class_data:
                        cmd_vel.angular.z = 0.3  # Turn right on paper
                        self.get_logger().info("Paper detected: Turning Right")
                    elif "Rock" in class_data:
                        cmd_vel.linear.x = 0.0  # If second rock after the first, stop
                        cmd_vel.angular.z = -0.5
                        self.moving = False  # Stop moving on its own
                        self.get_logger().info("Second Rock detected: Stopping")
                    else:
                        cmd_vel.angular.z = -0.5  # Carry on straight if no input
            else:
                cmd_vel.linear.x = 0.0
                cmd_vel.angular.z = -0.5  # Stop

# Original Code without "Rock" toggle (very janky and harder to control)
 #if "Rock" in class_data:
             #   cmd_vel.linear.x = 0.3  # Move forward
              #  cmd_vel.angular.z = -0.5
            #elif "Paper" in class_data:
             #   cmd_vel.linear.x = 0.3
              #  cmd_vel.angular.z = 0.0  # Turn
            #elif "Scissors" in class_data:
             #   cmd_vel.linear.x = 0.3
             #  cmd_vel.angular.z = -0.8  # Turn in the opposite direction
            #else:
                #cmd_vel.linear.x = 0.0
                #cmd_vel.angular.z = -0.5  # Stop



            # Publish the command
            self.cmd_vel_pub.publish(cmd_vel)

        except Exception as e:
            self.get_logger().error(f"Error during processing: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = hand_detection_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
