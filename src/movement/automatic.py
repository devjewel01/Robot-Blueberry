from expression import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

time.sleep(2)

def stop():
    print("stop")
    Stop()

def forward():
    Run(1, 0, 1, 0, 70)
    print("Forward")

def back():
    Start_Slow(0,1,0,1)
    Run(0, 1, 0, 1, 70)
    print("back")


def left():
    Run(0, 1, 1, 0, 70)
    print("left")


def right():
    Run(1, 0, 0, 1, 70)
    print("right")

stop()
count = 0
while True:
    i = 0
    avgDistance = 0
    for i in range(5):
        GPIO.output(TRIG, False) 
        time.sleep(0.1) 

        GPIO.output(TRIG, True)  
        time.sleep(0.00001) 
        GPIO.output(TRIG, False) 

        while GPIO.input(ECHO) == 0: 
            print("Echo 0")
        pulse_start = time.time()

        while GPIO.input(ECHO) == 1:  
            print("Echo 1")
        pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)  
        avgDistance = avgDistance+distance

    avgDistance = avgDistance/5
    print(avgDistance)

    flag = 0
    if avgDistance < 100: 
        count = count+1
        stop()
        time.sleep(1)
        back()
        time.sleep(1.5)
        if (count % 3 == 1) & (flag == 0):
            right()
            flag = 1
        else:
            left()
            flag = 0
        time.sleep(1.5)
        stop()
        time.sleep(1)
    else:
        forward()
        flag = 0
    time.sleep(2)
