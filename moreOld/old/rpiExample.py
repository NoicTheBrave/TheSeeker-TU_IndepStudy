#https://www.youtube.com/watch?v=eImDQ0PVu2Y
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
my_pwm=GPIO.PWM(33,1000) #  (Define pin frequency) 

my_pwm.start(10) #Tells what % of the duty cycle is being used (This is the core of the PWM, what you want to modulate that is, to my understanding) 


#my_pwm.ChangeDutyCycle(99)
time.sleep(10)
