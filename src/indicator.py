#!/usr/bin/env python

try:
    import RPi.GPIO as GPIO
except Exception as e:
    GPIO = None
import time
import os
from actions import configuration
import time
import threading
import numpy
import usb.core
import usb.util
from gpiozero import LED
try:
    import queue as Queue
except ImportError:
    import Queue as Queue


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Indicators
listeningindicator=configuration['Gpios']['assistant_indicators'][0]
speakingindicator=configuration['Gpios']['assistant_indicators'][1]

#Stopbutton
stoppushbutton=configuration['Gpios']['stop_pushbutton'][0]
GPIO.setup(stoppushbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(stoppushbutton,GPIO.FALLING)

GPIO.setup(listeningindicator, GPIO.OUT)
GPIO.setup(speakingindicator, GPIO.OUT)
GPIO.output(listeningindicator, GPIO.LOW)
GPIO.output(speakingindicator, GPIO.LOW)

def assistantindicator(activity):
    activity=activity.lower()
    if activity=='listening':
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.HIGH)
       
    elif activity=='speaking':
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.LOW)
        
    elif (activity=='off' or activity=='unmute'):
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.LOW)
        
    elif (activity=='on' or activity=='mute'):
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.HIGH)
        

