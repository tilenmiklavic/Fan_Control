#
# Fan_pin is board pin 7 or GPIO4
# relay is connected to the fan_pin
# fan is connected to the relay
#


import RPi.GPIO as GPIO
import time

#board pin 7 is the GPIO4
fan_pin = 7
critical_temp = 60
treshold = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.cleanup()

def return_temp():
	tFile = open('/sys/class/thermal/thermal_zone0/temp')
	temp = float(tFile.read())
	tempC = temp / 1000
	
	tFile.close()
	
	return tempC

def fan_on():
	print("CPU temperature: " + str(return_temp()) + "C")
	print("Fan on")
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(fan_pin, GPIO.OUT)
	
	while True:
		tempC = return_temp()
		
		if tempC > (critical_temp - treshold):
			GPIO.output(fan_pin, GPIO.HIGH)
		else:
			GPIO.output(fan_pin, GPIO.LOW)
			GPIO.cleanup()	
			break
			
		time.sleep(5)


while True:
	tempC = return_temp()
	time.sleep(2)
	
	if tempC > critical_temp:
		fan_on()
		