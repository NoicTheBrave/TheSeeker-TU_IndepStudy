import serial
import time

serial1 = serial.Serial('/dev/ttyACM0', 9600)
#message = "50" #example PWM # (0 -> 255) 

counter = 1 #must NOT start as 0 or 255
directionFlag = 0 # 0 = Up, 1 = Down 

while True:
	print(counter)
	serial1.write((str(counter)+ '\n').encode()) # New line character required, otherwise, messages with smaller time delays between one another DO NOT PROPERLY REGISTER (based on personal experience0 
	time.sleep(1)
	if(counter == 255):
		directionFlag = 1
	if(counter == 0):
		directionFlag = 0
	
	if(directionFlag == 1): #gotta go DOWN
		counter = counter - 1
	else: 
		counter = counter + 1 
	#serial1.write(b’9’)
	#time.sleep(1)


