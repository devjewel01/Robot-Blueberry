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
	    h.servo[i].angle=init[i]
	    time.sleep(0.5)

def takePositionSlow():
    for i in range(0, 12):
        changeDegree(i, init[i])
        time.sleep(0.05)

def hug():
	takePosition()
	time.sleep(1)
	#start
	changeDegree([7,10],[0,180])
	changeDegree([3,4],[90,90])
	changeDegree([2,5],[50,150])
	changeDegree([7,10],[50,130])
	changeDegree([6,9],[90,90])
	time.sleep(2)
	#stop
	changeDegree([7,10],[180,0])
	changeDegree([3,4],[0,180])
	changeDegree([2,5],[20,160])
	changeDegree([6,9],[170,10])
    takePositionSlow()

def hands_up():
	takePosition()
	changeDegree([10,7], [180,0])
    changeDegree([5,2], [40,140])
    changeDegree([4,3], [90,90])
    changeDegree([10,7], [130,70])
    time.sleep(2)
    changeDegree([10,7], [0,180])
    changeDegree([4,3], [180,0])
    changeDegree([5,2], [160,20])
    time.sleep(1)
    takePositionSlow()

def hand_shake():
    takePosition()
    #
    #
    takePositionSlow

def salute():
#salute
    takePosition()
    changeDegree(7,0)
    changeDegree(3,180)
    changeDegree(7,80)
    changeDegree(6,60)
#normal
    changeDegree(7,180)
    changeDegree(3,0)
    changeDegree(6,170)
    takePositionSlow()

def touch_head():
    takePosition()
    #
    #
    takePositionSlow()

def touch_nose():
    takePosition()
    #
    #
    takePositionSlow()

def touch_eye():
    takePosition()
    #
    #
    takePositionSlow()

def touch_ear():
    takePosition()
    #
    #
    takePositionSlow()



	


