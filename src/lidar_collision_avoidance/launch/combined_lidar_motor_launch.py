import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    sensor_pkg = 'ucsd_robocar_sensor2_pkg'
    some_package = 'ldlidar'
    some_node = 'ldlidar'  # Correct executable name
    some_config = 'ld06.yaml'

    # LiDAR sensor node (publishing scan data)
    sensor_node = Node(
        package=some_package,
        executable=some_node,  # Correct executable name for your LiDAR
        output='screen',
        parameters=[{
            'serial_port': '/dev/ttyUSB0',  # Ensure this matches the correct port
            'baud_rate': 230400  # Ensure the baud rate matches your LiDAR
        }]
    )

    # Lidar collision avoidance node (subscribing to scan data and publishing cmd_vel)
    collision_avoidance_node = Node(
        package='lidar_collision_avoidance',
        executable='lidar_collision_avoidance_node',
        output='screen'
    )

    # Motor controller node (vesc_twist_node)
    motor_controller_node = Node(
        package='ucsd_robocar_actuator2_pkg',  # Motor controller package
        executable='vesc_twist_node',  # Motor controller executable
        output='screen',
        parameters=[{
          #  'serial_port': '/dev/ttyUSB1',  # Ensure this is the correct port for your VESC
            'baud_rate': 115200  # Standard VESC baud rate
        }]
    )

    # Launch all nodes together
    return LaunchDescription([
        sensor_node,
        collision_avoidance_node,
        motor_controller_node  # Add motor controller node to the launch sequence
    ])


