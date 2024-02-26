import serial
import time

serial1 = serial.Serial('/dev/ttyACM1', 9600)
#message = "50" #example PWM # (0 -> 255) 

while True:
	message = str(input("State Number from 0 to 255:" ))
	serial1.write(message.encode())
	#time.sleep(0.1)
	#serial1.write(b’9’)
	#time.sleep(1)


