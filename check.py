import serial
import time
import os

# Set varibles
device = "/dev/ttyACM0"
rate = "9600"
checkFile = "test01"
loop = 1

# Open serial connection
ser = serial.Serial(device, rate, timeout=1)

# Wait for the connection to be opened
time.sleep(4)

# Main file checking loop
while(loop == 1):

	# If file exists else keep checking
	if os.path.exists(checkFile):
		
		# Read the data to send to the device
		data = open(checkFile,'r').read()
		
		# Write the data to the device
		ser.write(data)
		
		# Remove check file
		os.remove(checkFile)
	
	# Pause before checking again
	time.sleep(1)
	pass

# Close the serial connection
ser.close()
