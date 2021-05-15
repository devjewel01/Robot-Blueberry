import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


h = ServoKit(channels=16)


init = [90,0,180,0,170,170,0,180,0,60,150,0]
limit = [180,180,0,0,40,0,0,180,180,180,30,180]

cur = init

def changeDeg(pin1,new1,pin2,new2):
    now1 = cur[pin1]
    now2 = cur[pin2]
    for deg in range(0,max(abs(now1-new1),abs(now2-new2)),5):
        if now1<new1:
            now1=now1+5
        elif now1>new1:
            now1=now1-5
        if now2<new2:
            now2=now2+5
        elif now2>new2:
            now2=now2-5
        h.servo[pin1].angle=now1
        h.servo[pin2].angle=now2
        time.sleep(0.05)
    cur[pin1]=now1
    cur[pin2]=now2

    
for i in range(0,12):
    h.servo[i].angle = init[i]
time.sleep(1)    

changeDeg(8,180,7,0)
changeDeg(2,60,1,140)
changeDeg(4,90,3,90)
changeDeg(8,130,7,70)
time.sleep(2)
changeDeg(8,0,7,180)
changeDeg(4,170,3,0)
changeDeg(2,180,1,0)
time.sleep(2)

    
for i in range(0,12):
    h.servo[i].angle = init[i]

