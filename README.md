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
* DC Power Supply (5V output - External Supply needed for PCA9685 board in order to power servo(s?))
* Raspberry Pi Power Supply (for the Pi 3B or comperable power supply) 
* Female-to-Male Doupont Cables (@ minimum, 6-8 are recommended, additional cables are encouraged if buying))
* Female-to-Female Doupont Cables (@ minimum, 4 are needed)
* 22 gauge wire (Used for the PCA9685 board's external power connection - 2 male-to-male Doupont can be used if nessisary)

# Wiring: 
* Wiring the demo circuit is simple for connecting the Raspberry Pi to the PCA9685 board:
* * 5V -> VCC (optional - see below)
  * GND -> GND
  * SDA -> SDA
  * SCL -> SCL
* For a Pin-out of the Raspberry Pi and the headder pins used, please view the image below. The pins I used for this project are inside the blue rectangle:
![alt text](https://github.com/NoicTheBrave/TheSeeker-TU_IndepStudy/blob/main/images/rasPi_IndepStudyWiringDiagram.png?raw=true)

* (optional):
* * NOTE: You can technically on the PCA9685 board connect the V+ pin to the VCC pin, however, this is not recommended unless you are certain that your external power supply is operating at 5V. The VCC pin powers the chips on the PCA9685 board while the V+ pin is to power the GPIO 5V power pins for servos and other connected peripherials. (there is a reason the manufacturer did not simply connect these lines directly together. Use this tip with caution and @ your own discretion, I am not responcible for your actions :) 
* * https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all
  * WARNING: "The VCC pin is just power for the chip itself. If you want to connect servos or LEDs that use the V+ pins, you MUST connect the V+ pin as well. The V+ pin can be as high as 6V even if VCC is 3.3V (the chip is 5V safe). We suggest connecting power through the blue terminal block since it is polarity protected."
 
  * 


# notes - for the dev: 
* The core purpose of this thing is to be able to , idealy, preform ROS and cotnrol the car w/ ROS. Unfortunately, due to time constraints, I was not able to implement this on the Nvidia Jetsion, however, due to time constraints, this was the most time-efficient solution I developed. With this in mind, via USB-Serial and other methods, it is still possible to communicate and pass data from the Nvidia Jetson to the Raspberry Pi bidirectionally as need be. I believe there *is* some method avaliable for this software to operate on the Nvidia Jetsion for GPIO, however once more due to time constraints, was not able to explore that domain of the project, simply getting this operational was difficult as it was. 
