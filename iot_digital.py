#!/usr/bin/env python
import Netmaxiot   
from time import sleep
a=2
Netmaxiot.pinMode(a,"OUTPUT")
# Netmaxiot.pinMode(3,"OUTPUT")
# Netmaxiot.pinMode(4,"OUTPUT")
# Netmaxiot.pinMode(5,"OUTPUT")
# Netmaxiot.pinMode(6,"OUTPUT")
# Netmaxiot.pinMode(7,"OUTPUT")
# Netmaxiot.pinMode(8,"OUTPUT")
while 1:
	Netmaxiot.digitalWrite(a,1)
	# Netmaxiot.digitalWrite(3,1)
	# Netmaxiot.digitalWrite(4,1)
	# Netmaxiot.digitalWrite(5,1)
	# Netmaxiot.digitalWrite(6,1)
	# Netmaxiot.digitalWrite(7,1)
	# Netmaxiot.digitalWrite(8,1)
	print("on")
	sleep(0.2)
	Netmaxiot.digitalWrite(a,0)
	# Netmaxiot.digitalWrite(3,0)
	# Netmaxiot.digitalWrite(4,0)
	# Netmaxiot.digitalWrite(5,0)
	# Netmaxiot.digitalWrite(6,0)
	# Netmaxiot.digitalWrite(7,0)
	# Netmaxiot.digitalWrite(8,0)
	print("off")
	sleep(0.2)

	#analog  8 bit,12,24 adc ->___________ 0-255,0-1023,0-4096    we have 10bits_____0-1024
	# its measuer analog voltage 0-5v________resolution 0-1023