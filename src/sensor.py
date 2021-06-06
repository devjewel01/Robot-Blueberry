#!/usr/bin/env python

import sys
sys.path.append('/home/pi/Robot-Blueberry/src')

from talk import say
import RPi.GPIO as GPIO
import time
import os
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))


GPIO.setmode(GPIO.BCM)

gas = 4
fire = 27


GPIO.setup(fire, GPIO.IN)
GPIO.setup(gas, GPIO.IN)


def sensorOn():
    print("Sensor active")
    with open('{}/src/servo.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servo = yaml.load(conf, Loader=yaml.FullLoader)
        servo['Sensor']['gas'] = 'on'
        with open('{}/src/servo.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(servo,conf)
    say('activated  sensor')
    loop()
def loop():
    with open('{}/src/servo.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servo = yaml.load(conf, Loader=yaml.FullLoader)
        if(servo['Sensor']['gas'] == 'off'):
            return
        digFire = GPIO.input(fire)
        digGas = GPIO.input(gas)

        if digFire == 0 or digGas == 0: 
            warning = "Something is not okay"
            print(warning)
            say("Please check, there are something wrong")
        else:
            print("Nothing found")
        time.sleep(2)
    loop()

def sensorOff():
    print("Stor sensor")
    with open('{}/src/servo.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servo = yaml.load(conf, Loader=yaml.FullLoader)
        servo['Sensor']['gas'] = 'off'
        with open('{}/src/servo.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(servo,conf)
    say('deactivated sensor')



