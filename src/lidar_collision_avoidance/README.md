README.md

Purpose: Moves the robot forward until it reaches an obstacle. When the lidar detects an obstacle it stops the robot until the obstacle is removed. 

Setup:

ssh -X jetson@ucsdrobocar-team-5
source ~/.bashrc

docker start lidar_collision_test
docker exec -it lidar_collision_test bash

Details:
Files are located in /home/projects/ros2/src


To Run Package:
source_ros2
build_ros2

ros2 launch lidar lidar_collision_avoidance lidar_collision_avoidance_launch.py