#!/usr/bin/env python

import os
import os.path
import yaml
import time

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from adafruit_servokit import ServoKit

Motor1 = {'EN': 27, 'input1': 19, 'input2': 16}
Motor2 = {'EN': 22, 'input1': 26, 'input2': 20}

for x in Motor1:
    GPIO.setup(Motor1[x], GPIO.OUT)
    GPIO.setup(Motor2[x], GPIO.OUT)

EN1 = GPIO.PWM(Motor1['EN'], 100)    
EN2 = GPIO.PWM(Motor2['EN'], 100)    

EN1.start(0)                    
EN2.start(0)  


hand = ServoKit(channels=16)

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))

def readYaml():
    with open('{}/src/configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servo = yaml.load(conf, Loader=yaml.FullLoader)
    return servo


def writeYaml(s=None):
    with open('{}/src/configuration.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
        if s==None:
            yaml.dump(servo,conf)
        else:
            yaml.dump(s,conf)


servo = readYaml()

if servo == None:
    with open('{}/src/configurationBackUp.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servoBackUp = yaml.load(conf, Loader=yaml.FullLoader)
    writeYaml(servoBackUp)
    servo = readYaml()
    if servo == None:
        print('close')
        exit()


Initial = servo['Initial_Position']['I2C']
Current = servo['Current_Position']['I2C']

InitialGpio = servo['Initial_Position']['Gpio']
CurrentGpio = servo['Current_Position']['Gpio']
GpioPin     = servo['Pin']['Gpio']
I2CPin      = servo['Pin']['I2C']


for i in range(0,6):
    GPIO.setup(GpioPin[i], GPIO.OUT)
Servo = []
for i in range(0,6):
    Servo.append(GPIO.PWM(GpioPin[i],50))
    Servo[i].start(0)


def changeDegree(pin,newDegree,time1=0.05,time2=0):
    maxChange = 0
    pinSize = len(pin)
    for i in range(0,pinSize):
        maxChange = max(abs(Current[pin[i]]-newDegree[i]),maxChange)
    for deg in range(0,maxChange,5):
        for i in range(0,pinSize):
            if Current[pin[i]]<newDegree[i]:
                Current[pin[i]] += 5
            elif Current[pin[i]]>newDegree[i]:
                Current[pin[i]] -= 5

        for i in range(0,pinSize):
            hand.servo[pin[i]].angle = Current[pin[i]]
            servo['Current_Position']['I2C'][pin[i]] = Current[pin[i]]
        writeYaml()
        time.sleep(time1)

        
def takePosition():
    changeDegree([7,8],[180,0])
    changeDegree(I2CPin,Initial)


def changeDegreeGpio(pin,degree,update,duration):
    pinSize = len(pin)
    for i in range(0,pinSize):
        p = pin[i]
        if CurrentGpio[p]>degree[i]:
            update = -update

        for deg in range(CurrentGpio[p],degree[i],update):
            duty = deg/18
            duty+=2
            Servo[p].ChangeDutyCycle(duty)
            time.sleep(duration)
        CurrentGpio[p]=degree[i]
        writeYaml()


def Run(a, b, c, d, x):
    GPIO.output(Motor1['input1'], GPIO.LOW)
    GPIO.output(Motor1['input2'], GPIO.LOW)
    GPIO.output(Motor2['input1'], GPIO.LOW)
    GPIO.output(Motor2['input2'], GPIO.LOW)

    if a==1:
        GPIO.output(Motor1['input1'], GPIO.HIGH)
    if b==1:
        GPIO.output(Motor1['input2'], GPIO.HIGH)
    if c==1:
        GPIO.output(Motor2['input1'], GPIO.HIGH)
    if d==1:
        GPIO.output(Motor2['input2'], GPIO.HIGH)

    EN2.ChangeDutyCycle(x)
    EN1.ChangeDutyCycle(x)


def Stop():
    Run(0,0,0,0,0)


def Start_Slow(a, b, c, d):
    for i in range(0,100,20):
        Run(a,b,c,d,i)
        time.sleep(0.5)

    
def Stop_Slow(a,b,c,d):
    for i in range(100,0,-20):
        Run(a,b,c,d,i)
        time.sleep(0.5)


def yes(times=3):
    for i in range(0,times):
        changeDegree([0],[30])
        time.sleep(0.08)
        changeDegree([0],[0])
        time.sleep(0.08)

def no(times=3):
    for i in range(0,times):
        changeDegreeGpio([0],[70],5,0.05)
        time.sleep(0.2)
        changeDegreeGpio([0],[110],5,0.05)
        time.sleep(0.2)
    changeDegreeGpio([0],[90],5,0.05)

def move_head(times=3):
    for i in range(0,times):
        changeDegree([0],[20])
        changeDegreeGpio([0],[80],5,0.05)
        changeDegree([0],[0])
        changeDegreeGpio([0],[100],5,0.05)

