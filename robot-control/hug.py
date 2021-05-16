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
#start

changeDeg([7,8],[0,180])
changeDeg([3,4],[90,90])
changeDeg([1,2],[50,150])
changeDeg([7,8],[50,130])
changeDeg([5,6],[90,90])
time.sleep(2)
#stop
changeDeg([7,8],[180,0])
changeDeg([3,4],[0,180])
changeDeg([1,2],[20,160])
changeDeg([5,6],[170,10])