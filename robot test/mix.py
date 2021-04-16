import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)

kit = ServoKit(channels=16)

servo1.ChangeDutyCycle(12)
time.sleep(1)
servo1.ChangeDutyCycle(12)



kit.servo[0].angle = 180
time.sleep(1)
kit.servo[0].angle = 0

