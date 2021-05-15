import time
from adafruit_servokit import ServoKit

h = ServoKit(channels=16)

while True:
	n = (int)(input("servo no : "))
	d = (int)(input("enter degree : "))
	h.servo[n].angle = d
