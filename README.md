# TheSeeker-TU_IndepStudy
Repo is made for the Independent Study I did w/ Dr. Nathan Hutchins for Spring 2024 on an autonomous driving vehicle with a payload. Tracking via OptiTrack and additional sensors plan to be incorporated. 

------------------
# Install:
For this demo, I used a Raspberry Pi inorder to control the steering servo of the car w/ a solution for controlling the ESC (speed controller) of the car (Not implemented, but discussed in documentation).

* Do NOT use the install file provided, it is a legacy item. Follow the following video to install all the packages and Image file you need for this project: https://www.youtube.com/watch?v=iLiI_IRedhI&list=PLuteWQUGtU9BU0sQIVqRQa24p-pSBCYNv&index=4
* * The Video provides you where to install the image file needed to be used for the Raspberry Pi, How to set up the ROS environment, and how to move one of the servos (software) via ROS.


# Hardware Requirements: 
* Raspberry Pi 3B (3B+ according to the image file's host site, can be used, Ras Pi 4B does NOT work, despite what Eit tells you)
* PCA9685 16 Channel PWM Servo Driver Board (12 bit IIC Interface Module Compatible with Arduino and Raspberry Pi)
* DC Power Supply (5V output - External Supply needed for
* Raspberry Pi Power Supply (for the Pi 3B or comperable power supply) 
* Female-to-Male Doupont Cables (@ minimum, 6-8 are recommended, additional cables are encouraged if buying))
* Female-to-Female Doupont Cables (@ minimum, 4 are needed)
* 22 gauge wire (Used for the PCA9685 board's external power connection - 2 male-to-male Doupont can be used if nessisary)

