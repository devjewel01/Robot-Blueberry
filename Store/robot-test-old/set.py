
import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit




def changeDeg(pin1,new1):
    now1 = cur[pin1]
    for deg in range(0,abs(now1-new1),5):
        if now1<new1:
            now1=now1+5
        elif now1>new1:
            now1=now1-5
        h.servo[pin1].angle=now1
        time.sleep(0.05)
    cur[pin1]=now1
while True:
    changeDeg((int)(input("pin ")),(int)(input("deg ")))
    