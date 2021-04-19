import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def call(channel):
	print("You press the button. ")

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=call)

i=0
while True:
	i++
	print(i)
	time.sleep(0.5)

