<div id="top"></div>

<h1 align="center">MAE148 Team F1 Trillion</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://jacobsschool.ucsd.edu/">
    <img src="images\UCSDLogo_JSOE_BlueGold.png" alt="Logo" width="400" height="100">
  </a>
<h3>MAE148 Final Project</h3>
<p>
Summer Session 2 - Team 5: Color/Shape, Boundary, and Collision Recognition (Camera, LiDAR, GNSS)
</p>

<!--Insert image of team car here-->
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



<!-- TEAM MEMBERS -->
## Team Members

<h4>Team Member Major and Class </h4>
<ul>
  <li>Adem Evecek - Mechanical Engineering</li>
  <li>Alexa Nordstrom - Electrical and Computer Engineering</li>
  <li>Reggie Estrella - Mechanical Engineering</li>
  <li>Parissa Teli - Mechanical Engineering</li>
</ul>

<!-- Final Project -->
## Final Project
  <p>The original goal was to use AI object detection paired with the OAK-D camera to build a model that recognizes basic street signs and color images from the camera. Based on how the AI model classifies these different objects and colors, the AI would then tell the autonomous car to react accordingly to the specific sign or color detected. The signs and colors would be placed on a track we planned, we would then pair the GNSS to set an origin on the track where the car would stop, start, and prevent the car from going out of bounds from our track. Additionally to using the camera and GNSS sensors, we wanted to include the Lidar to prevent the autonomous vehicle from running into objects, it was planned to prevent it from running into an object if an object was detected within a foot of it.<p>
  <p>Due to the limitations of time of taking MAE 148 during the summer, we had to change the goal of our project to using rock, paper, scissors to direct our car instead. With the new goal of our project, we still used an AI model and the OAK-D camera for object detection. We built a model that recognizes the hand signals rock, paper, scissors to control our autonomous vehicle instead. The car will start from rest until the camera sees the hand signal for rock, when rock is detected the first time, the car drives straight. When detecting the hand signal scissors, the car will steer left, when detecting the hand signal paper, the car will steer right. When the car detects rock again, it will stop driving. Our goal with the lidar and GNSS was still kept.<p>


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

See [`README`](docker/README.md) section in our `docker` directory for breakdown of how to run the Docker container for our program with all dependencies built into the image

### Our Hopes and Dreams
#### Stretch Goal 1


### Final Project Documentation

* [Final Project Proposal](https://docs.google.com/presentation/d/199oVWJiOSEHAjcmizN8rejuzU7rHNCNl4qY55uGqgxQ/edit?usp=sharing)
* [Progress Update 2/29](https://github.com/kiers-neely/ucsd-mae-148-team-4/files/14469441/mae148-slides-update.pdf)
* [Progress Update 3/7](https://github.com/kiers-neely/ucsd-mae-148-team-4/files/14547470/mae148-slides-update.2.pdf)

<!-- Early Quarter -->
## Robot Design

### CAD Parts
#### Final Assembly

#### Custom Designed Parts


#### Open Source Parts
- Jetson Nano Case: https://www.printables.com/model/395600-jetson-nano-case
- 

### Electronic Hardware


### Software
#### Embedded Systems

#### ROS2

#### DonkeyCar AI

<!-- Authors -->
## Authors

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



