import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


'''GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)'''

h = ServoKit(channels=16)

#servo1.ChangeDutyCycle(12)
#kit.servo[0].angle 

init = [0,90,20,0,180,160,170,180,60,0,0,150]
limitLo = [0,0,20,0,0,40,0,0,60,0,0,30]
limitHi = [35,180,180,180,180,160,170,180,180,180,180,150]

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


#start
changeDeg(7,80)
changeDeg(3,140)
changeDeg(1,30)
changeDeg(5,90)
changeDeg(9,0)
time.sleep(3)
#normal
changeDeg(9,60)
changeDeg(7,180)
changeDeg(5,170)
changeDeg(1,0)
changeDeg(3,0)