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

def changeDeg(pin , new):
    if(new<cur[pin]):
        #new = max(new,limitLo[pin])
        for i in range(cur[pin],new-1,-5):
            h.servo[pin].angle = i
            time.sleep(0.05)
    else:
        #new = min(new,limitHi[pin])
        for i in range(cur[pin]+1,new,5):
            h.servo[pin].angle=i
            time.sleep(0.05)
    cur[pin]=new
for i in range(0,12):
    h.servo[i].angle=init[i]
    time.sleep(0.05)
#up
changeDeg(3,60)
changeDeg(7,150)
time.sleep(0.5)
#shake
for i in range(0,5):
    if i&1:
        h.servo[7].angle=170
    else:
        h.servo[7].angle=120
    time.sleep(0.2)
time.sleep(1)
#down
changeDeg(7,180)
changeDeg(3,0)

time.sleep(2)

for i in range(0,12):
    print(cur[i]," ",init[i])
    changeDeg(i,init[i])


