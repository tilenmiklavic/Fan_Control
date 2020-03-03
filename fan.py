from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time

#board pin 7 is the GPIO4
fan_pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin, GPIO.OUT)

while True:
	print("Checking the CPU temperature...")
	cpu = CPUTemperature()
	
	if cpu.temperature > 50:
		 fan_on()
		 time.sleep(5)
		 fan_off()
	

def fan_on():
	GPIO.output(fan_pin, GPIO.HIGH)
	print("CPU temperature: " + "C")
	print("Fan on")
	
def fan_off():
	GPIO.output(fan_pin, GPIO.LOW) 
	#print("CPU temperature: ")
	print("Fan off")
