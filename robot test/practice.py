import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(17,50)
servo1.start(2)

time.sleep(1)


