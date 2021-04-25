import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


'''GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)'''

h = ServoKit(channels=16)

'''
servo move demo
servo1.ChangeDutyCycle(12) for gpio pin 
kit.servo[0].angle = angle for I2C 

'''

init = [0,90,20,0,180,160,170,180,60,0,0,150]
limit = [35, 180, 0, 180, 140, 180, 180, 180, 180, 180, 180, 180]
cur = init

    
def changeDegree(pin,newDegree):
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

def takePosition():
    for i in range(0,12):
        h.servo[i].angle = init[i]
        time.sleep(0.05)

def takePositionSlow():
    for i in range(0,12):
        changeDegree(i,init[i])
       

#up
changeDeg([3],[60])
changeDeg([7],[150])
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
changeDeg([7],[180])
changeDeg([3],[0])
