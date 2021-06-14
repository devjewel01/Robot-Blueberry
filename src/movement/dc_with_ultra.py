from expression import *
# programming the GPIO by BCM pin numbers

#TRIG = servo['Sensor']['ultrasonic']['trigger']
#ECHO = servo['Sensor']['ultrasonic']['echo']
TRIG = 24
ECHO = 23

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input                

def forward():
    Run(1,0,1,0,80)

def back():
    Run(0,1,0,1,80)

def left():
    Run(0,1,1,0,80)

def right():
    Run(1,0,0,1,80)

Stop()
count=0
def Distance():
    avgDistance=0
    for i in range(2):
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        time.sleep(0.1)                                   #Delay

        GPIO.output(TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                           #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        off=1
        while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
            pass
        pulse_start = time.time()
        off=0
        while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
            pass
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
        distance = round(distance,2)                 #Round to two decimal points
        avgDistance=avgDistance+distance
    return avgDistance
while True:
    i=0
    avgDistance=Distance()/5
    time.sleep(1)
    flag=0
    if avgDistance < 100:
        count += 1      #Check whether the distance is within 15 cm range
        Stop()
        time.sleep(2)
        changeDegreeGpio([0],[0],5,0.05)
        dist = Distance()/5
        print("right dist ",dist)
        time.sleep(8)
        if dist>=5:
            right()
            continue
        changeDegreeGpio([0],[180],5,0.05)
        dist = Distance()/5
        print("left dist ",dist)
        time.sleep(8)
        if dist>=5:
            left()
            continue
        changeDegreeGpio([0],[90],5,0.05)
        time.sleep(1)
        back()
        time.sleep(1.5)
        if (count%3 ==1) & (flag==0):
            right()
            flag=1
        else:
            left()
            flag=0
        time.sleep(1.5)
        stop()
        time.sleep(1)
    else:
        print("go forward")
        flag=0

