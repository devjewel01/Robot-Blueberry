import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

while True:
	state = GPIO.input(18)
	if state = True:
		print("Motion detected")
		time.sleep(1)


