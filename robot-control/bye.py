import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


h = ServoKit(channels=16)

init = [90,0,180,0,170,170,0,180,0,60,150,0]
limit = [35, 180, 0, 180, 140, 180, 180, 180, 180, 180, 180, 35]
cur = init

cur = init

def changeDeg(pin,newDegree):
    maxChange = 0
    pinSize = len(pin)
    for i in range(0,pinSize):
        maxChange = max(abs(cur[pin[i]]-newDegree[i]),maxChange)
    for deg in range(0,maxChange,5):
        for i in range(0,pinSize):
            if cur[pin[i]]<newDegree[i]:
                cur[pin[i]] += 5
            elif cur[pin[i]]>newDegree[i]:
                cur[pin[i]] -= 5

        for i in range(0,pinSize):
            h.servo[pin[i]].angle = cur[pin[i]]
        time.sleep(0.05)
#function closed
for i in range(0,12):
    h.servo[i].angle=init[i]
time.sleep(1)

changeDeg([7,9,3,5,1],[60,0,60,180,50])
time.sleep(0.5)
changeDeg([5],[160])
changeDeg([5],[180])
changeDeg([5],[160])
changeDeg([5],[180])
changeDeg([5],[160])
changeDeg([5],[180])
time.sleep(1)
changeDeg([5,9,3,7,1],[170,60,0,180,0])
