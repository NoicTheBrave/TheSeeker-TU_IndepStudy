import serial 
import time

def sendData(port, data): 
	ser = serial.Serial(port, 9600, timeout = 1) #open the serial port
	
	try: 
		ser.write(data.encode())
		print("Sent data: " + str(data)) 
	finally: 
		ser.close() #close serial port 

#main function 

serialPort = "/dev/ttyUSB0" #whatever the arduino's port is -_- 
data_to_send = input("Enter your data here (number 0-255): ") 

sendData(serialPort, data_to_send)

