<div id="top"></div>

<h1 align="center">MAE148 Team 5 - F1 Trillion</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>MAE148 Final Project</h3>
<p>
Summer Session 2 - Team 5: Shape/Color, Collision, and Boundary Recognition (OAKD Camera, LiDAR, GNSS)
</p>

<img src="images\GroupPic.png">
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#team-members">Team Members</a></li>
    <li><a href="#final-project">Final Project</a></li>
      <ul>
        <li><a href="#original-goals">Original Goals</a></li>
          <ul>
            <li><a href="#goals-we-met">Goals We Met</a></li>
            <li><a href="#our-hopes-and-dreams">Our Hopes and Dreams</a></li>
              <ul>
                <li><a href="#stretch-goal-1">Stretch Goal 1</a></li>
                <li><a href="#stretch-goal-2">Stretch Goal 2</a></li>
              </ul>
          </ul>
        <li><a href="#final-project-documentation">Final Project Documentation</a></li>
      </ul>
    <li><a href="#robot-design">Robot Design </a></li>
      <ul>
        <li><a href="#cad-parts">CAD Parts</a></li>
          <ul>
            <li><a href="#final-assembly">Final Assembly</a></li>
            <li><a href="#custom-designed-parts">Custom Designed Parts</a></li>
            <li><a href="#open-source-parts">Open Source Parts</a></li>
          </ul>
        <li><a href="#electronic-hardware">Electronic Hardware</a></li>
        <li><a href="#software">Software</a></li>
          <ul>
            <li><a href="#embedded-systems">Embedded Systems</a></li>
            <li><a href="#ros2">ROS2</a></li>
            <li><a href="#donkeycar-ai">DonkeyCar AI</a></li>
          </ul>
      </ul>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
videos {
  display: flex;
  gap: 40px;
}
@media only screen and (max-width: 1100px) {
  .videos {
    flex-direction: column;
  }
}

<!-- TEAM MEMBERS -->
## Team Members

<h4>Team Member Major and Class </h4>
<ul>
  <li>Adem Evecek - Mechanical Engineering</li>
  <li>Alexa Nordstrom - Electrical and Computer Engineering</li>
  <li>Parissa Teli - Mechanical Engineering</li>
  <li>Reggie Estrella - Mechanical Engineering</li>
</ul>

<!-- Final Project -->
## Final Project
### How Our Goals Changed
  <p>The original goal was to use an AI object detection paired with the OAK-D camera to build a model that recognizes basic street signs (arrows and shapes) and colored objects from the camera. Based on how the AI model classifies these different objects and colors, the AI would tell the autonomous car to react accordingly to the specific sign or color detected. The signs and colors would be placed on a dynamic track we planned, then we would pair the GNSS to set an origin on the track where the car would start, preventing the car from going beyond a radius from said origin. Additionally to using the camera and GNSS sensors, we wanted to include the Lidar to prevent the autonomous vehicle from running into stray obstacles. It was planned to prevent it from running into an object if an object was detected within a foot of it.<p>
  <p>Due to the time limitations of taking MAE 148 during the summer, we had to pivot our project goals to recognize hand signals, using rock, paper, and scissors symbols to direct our car instead. With the new goal of our project, we still used an AI model and the OAK-D camera for hand signal recognition to direct the car. When the program is started, the car remains in a stationary mode until it detects a rock hand signal. After that, the car moves at a constant velocity for 3 seconds, where it will not accept any other input to avoid inputting rock twice on accident. After this period, the car will search for further input while still moving forward at the same velocity. If it detects a paper or scissors input, the car will turn right or left respectively. If it detects a rock after the 3-second period, the car will come to a stop and wait for another rock input to start again. Our goal with the lidar and GNSS was still kept.<p>

<!-- Original Goals -->
### Original Goals
- Robot will recognize colors/shapes (Later changed to hand signals) using the stereo vision camera
  - Camera will be used to recognize color/shape and react accordingly to follow a dynamic course we lay out 
- GNSS
  - Sets an origin at the start and stays within a certain distance from said point
- Lidar
  - Used for anti-collision
- Traps/Speed Boosts
  - Robot recognizes and avoids objects that represent traps and goes through objects that represent speed boosts. When passing these “speed boosts,” the car will speed up for a duration of time. 
- Reach Goal: Cannon
  - At the end of a course, car recognizes a target, positions itself accordingly and fires a marble at the target
   
<!-- End Results -->
### Goals We Met
- 

See [`README`](src/README.md) section in our `src` directory for breakdown of how our packages run together


### Our Hopes and Dreams
#### Stretch Goal 1

### Car In Action

https://github.com/user-attachments/assets/ef5bdd65-9847-4e44-9062-f650a0391855

https://github.com/user-attachments/assets/609624b2-e438-4ed6-8b3d-a47af00dfec2

### LiDAR In Action

https://github.com/user-attachments/assets/3b33167a-7553-4b75-b4fb-097402140350

### Final Project Documentation

* [Final Project Proposal]()
* [Progress Update 9/3](https://docs.google.com/presentation/d/1g33PE9AXjGcXSfOKlIWwQ00itkMUI3Xohn7YYAK-YBs/edit?usp=sharing)
* [Final Project Presentation 9/6](https://docs.google.com/presentation/d/1Kh5DuJ2OJTZT9KIFtTjcRsvLP3D4vm2SrYZrtaFCOiI/edit?usp=sharing)

<!-- Early Quarter -->
## Robot Design
### CAD Parts
#### Final Assembly
<img src="images\FinalAssembly.png">

#### Custom Designed Parts
- LIDAR Mount (Alexa)
<img src="images\LIDARMount.png" width="200px" height="auto">
- GNSS Mount (Parissa)
<img src="images\GNSSMount.png" width="200px" height="auto">  
- Camera Stand (Alexa)
<img src="images\CameraCase_01.png" width="200px" height="auto">
- Camera Case (Alexa)
<img src="images\CameraCase_02.png" width="200px" height="auto">
- GPS Stand (Parissa)
<img src="images\GPSStand.png" width="200px" height="auto">
- GPS Receiver Mount (Alexa)
<img src="images\GPSReceiverMount.png" width="200px" height="auto">
- Side Plate Cover (Alexa)
<img src="images\SidePlateCover.png" width="200px" height="auto">
- Base Plate (Adem)
<img src="images\BasePlate.png" width="200px" height="auto">

#### Open Source Parts
- Jetson Nano Case: https://www.printables.com/model/395600-jetson-nano-case

### Electronic Hardware
<p>For our final project and classwork, we used an NVIDIA Jetson Nano as the embedded computer provided by the course. The Jetson Nano was chosen for its ability to run AI models for tasks such as image classification, object detection, segmentation, and speech processing, all in a compact and energy-efficient form factor. This provided our class with a wide range of learning opportunities and final project possibilities. To run object detection models on the Jetson Nano, we utilized an OAK-D Lite camera to process image data. The OAK-D Lite is a depth camera with an integrated AI processor that provides accurate short- and long-range stereo depth perception. This capability makes it well-suited for robotic vision applications and running AI models directly on the device. Additionally, we used an LD06 LiDAR sensor to detect nearby objects. The LD06 LiDAR offers 360-degree laser scanning using Direct Time-of-Flight (DTOF) technology, which allows it to measure distances to surrounding objects with high precision. We also integrated a GNSS receiver and antenna to receive and process signals from navigation satellites, enabling precise positioning and navigation for the autonomous vehicle. Finally, we employed a VESC (Vedder Electronic Speed Controller) to control the speed and direction of the motors and servos on the autonomous vehicle. The VESC motor controller utilizes Proportional-Integral-Derivative (PID) control algorithms and ROS 2 commands to manage vehicle dynamics effectively.<p>

### Software
<p>ROS 2 (Robot Operating System 2) is a set of open-source software libraries and tools for developing robotics applications, which we extensively utilized throughout the class. All of our ROS 2 code, packages, and nodes were organized within a Docker container, which we accessed and ran on our Jetson Nano. To interact with the Jetson Nano, we used a terminal on a VMware virtual machine. We developed two custom ROS 2 packages: a hand detection package and a LiDAR obstacle detection package. The hand detection package integrated with Roboflow to access the AI model we used for our autonomous vehicle. Both packages communicated with the VESC ROS 2 package provided within the Docker container, which enabled us to control the speed and direction of the vehicle via the VESC motor controller.<p>

#### Embedded Systems

#### ROS2

#### DonkeyCar AI

<!-- Authors -->
## Authors
Adem, Alexa, Reggie, and Parissa

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


<!-- CONTACT -->
## Contact

* Adem Evecek - aevecek@gmail.com
* Alexa Nordstrom - AlexaN2896@gmail.com
* Reggie Estrella - rege2021@gmail.com
* Parissa Teli - pikie.teli@gmail.com



