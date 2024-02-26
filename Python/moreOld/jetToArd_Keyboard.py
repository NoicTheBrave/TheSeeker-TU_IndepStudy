import serial
import time

serial1 = serial.Serial('/dev/ttyACM0', 9600)
#message = "50" #example PWM # (0 -> 255) 

while True:
	message = str(input("Use S### or T### to specify speed or turn angle \n S = Speed (0 -> 255), T = Turn (0-> 180): " ))
	serial1.write(message.encode())
	#time.sleep(0.1)
	#serial1.write(b’9’)
	#time.sleep(1)


