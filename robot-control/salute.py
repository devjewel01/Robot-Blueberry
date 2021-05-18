import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


h = ServoKit(channels=16)


init = [90,0,180,0,170,170,0,180,0,60,150,0]
limit = [35, 180, 0, 180, 140, 180, 180, 180, 180, 180, 180, 35]
cur = init

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
for i in range(0,12):
   h.servo[i].angle=init[i]


#start
changeDeg(7,0)
changeDeg(3,180)
changeDeg(7,80)
changeDeg(5,60)
time.sleep(2)
#normal
changeDeg(7,180)
changeDeg(3,0)
changeDeg(5,170)