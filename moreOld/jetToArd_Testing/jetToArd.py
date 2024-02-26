import serial
import time

serial1 = serial.Serial('/dev/ttyACM0', 9600)
message = "50" #example PWM # (0 -> 255) 

while True:

	serial1.write(message.encode())
	time.sleep(1)
	#serial1.write(b’9’)
	#time.sleep(1)


