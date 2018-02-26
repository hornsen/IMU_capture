
""" This is a Python script that was made to listen and save output from an Arduino """


# pySerial needs to be installed 
import serial
import unicodedata


serial_port ='/dev/ttyACM0'
write_to_file_path = 'output.data'
baud_rate = 19200 #In arduino, Serial.begin(baud_rate)

output_file = open(write_to_file_path, 'w+')
ser = serial.Serial(serial_port, timeout=None, baudrate=19200, xonxoff=False, rtscts=False, dsrdtr=False) 

while True:
	if ser.in_waiting > 0:
		line = ser.readline()

	try:
		line = line.decode('utf-8', errors='ignore') #ser.readline returns a binary, convert to string
		print(line)
		output_file.write(line)
	except:
		continue

