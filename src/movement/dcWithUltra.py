from expression import *
from move import changeDegreeGpio                 # programming the GPIO by BCM pin numbers

TRIG = 24
ECHO = 23

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input                

def forward():
    Run(1,0,1,0,50)

def back():
    Run(0,1,0,1,50)

def left():
    Run(0,1,1,0,100)

def right():
    Run(1,0,0,1,100)

Stop()
count=0
def Distance():
    avgDistance=0
    for i in range(5):
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        time.sleep(0.1)                                   #Delay

        GPIO.output(TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                           #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                 #Set TRIG as LOW

        while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
            pass            
        pulse_start = time.time()

        while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
            pass
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
        distance = round(distance,2)                 #Round to two decimal points
        avgDistance=avgDistance+distance
    return avgDistance
def isLeftPossible():
    changeDegreeGpio([0],[0],5,0.05)
    dist = Distance()/5
    if dist>=50:
        return True
    else:
        return False
def isRightPossible():
    changeDegreeGpio([0],[180],5,0.05)
    dist = Distance()/5
    if dist>=50:
        return True
    else:
        return False
while True:
    i=0
    avgDistance=Distance()/5
    flag=0
    if avgDistance < 100:      #Check whether the distance is within 15 cm range
        count=count+1
        Stop()
        time.sleep(1)
        if isLeftPossible()==True:
            left()
        elif isRightPossible()==True:
            right()
        else:
            left()
            left()
    else:
        #forward()
        print("forward")
        flag=0

