# **Lidar Collision Avoidance**

## **Overview**
**Purpose:**  
This package enables a robot to move forward until it reaches an obstacle. When the LiDAR sensor detects an obstacle, the robot stops until the obstacle is removed, at which point it resumes forward movement.

**Notes:**  
You can find additional documentation and detailed information here: [Google Docs - Lidar Collision Avoidance](https://docs.google.com/document/d/1VHQcTIyBjwy3DfpB9f3TBZ0Q-jcx_eLJVC8xMbHrpH8/edit?usp=sharing)

---

> ## **Setup**
> 
> 1. **SSH into the Jetson board**  
>    Use the following command to access the Jetson board:
> 
>    ```bash
>    ssh -X jetson@ucsdrobocar-team-5
>    ```
> 
> 2. **Source your environment**  
>    Once you’re logged in, ensure that your ROS2 environment is correctly sourced:
> 
>    ```bash
>    source ~/.bashrc
>    ```
> 
> 3. **Start the Docker container**  
>    Start the `lidar_collision_test` Docker container:
> 
>    ```bash
>    docker start lidar_collision_test
>    docker exec -it lidar_collision_test bash
>    ```

---

> ## **Details**
> 
> The relevant files for this package are located in the following directory on the Jetson board:
> 
> ```bash
> /home/projects/ros2/src
> ```
> 
> You can access and modify the files from there as needed.

---

> ## **How to Run the Package**
> 
> 1. **Source ROS2**  
>    Before running the package, make sure ROS2 is properly sourced:
> 
>    ```bash
>    source_ros2
>    ```
> 
> 2. **Build the package**  
>    Build the ROS2 package using:
> 
>    ```bash
>    build_ros2
>    ```
> 
> 3. **Launch the package**  
>    Finally, launch the LiDAR collision avoidance node using the following command:
> 
>    ```bash
>    ros2 launch lidar lidar_collision_avoidance lidar_collision_avoidance_launch.py
>    ```

---

This will display the sections with a blockquote effect (which is similar to a box) on GitHub:

1. **Setup**
2. **Details**
3. **How to Run the Package**
