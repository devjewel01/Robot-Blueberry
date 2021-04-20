import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


h = ServoKit(channels=16)

direction = [1, 2, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1]
init = [0,90,20,0,180,160,170,180,60,0,0,150]
limit = [35,180,180,180,0,40,0,0,180,180,180,30]

cur = [0,90,20,0,0,160,170,180,60,0,0,150]

def changeDeg(pin , new):
    if(new<cur[pin]):
        for i in range(cur[pin],new-1,-5):
            h.servo[pin].angle = i
            time.sleep(0.05)
    else:
        for i in range(cur[pin]+1,new,5):
		h.servo[pin].angle=i
            time.sleep(0.05)
    cur[pin]=new
    
for i in range(0,12):
    h.servo[i].angle = init[i]
    
#code write here
    
for i in range(0,12):
    h.servo[i].angle = init[i]


