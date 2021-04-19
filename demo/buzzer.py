import RPi.GPIO as GPIO
import time

buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

def buzz(pitch, duration):
	period = 1.0/pitch
	delay = period/2
	cycles = int(duration * pitch)
	for i in range(cycles):
		GPIO.output(buzzer_pin, True)
		time.sleep(delay)
		GPIO.output(False)
		time.sleep(delay)

while  True:
	pitch_s = intput("Enter pitch (200 to 2000): ")
	pitch = float(pitch_s)
	duration_s = input("Enter duration (seconds): ")
	duration = int(duration_s)
	buzz(pitch, duration)
