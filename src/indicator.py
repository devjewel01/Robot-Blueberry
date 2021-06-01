#!/usr/bin/env python

from arduino import get_command
import RPi.GPIO as GPIO
from moveGoogle import yes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Indicators
listeningindicator=5
speakingindicator=6

GPIO.setup(listeningindicator, GPIO.OUT)
GPIO.setup(speakingindicator, GPIO.OUT)
GPIO.output(listeningindicator, GPIO.LOW)
GPIO.output(speakingindicator, GPIO.LOW)

def assistantindicator(activity):
    activity=activity.lower()
    
    if activity=='listening':
        get_command(activity)
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.HIGH)
        yes(2)
       
    elif activity=='speaking':
        get_command(activity)
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.LOW)
        
    elif (activity=='off' or activity=='unmute'):
        get_command(activity)
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.LOW)
        
    elif (activity=='on' or activity=='mute'):
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.HIGH)
    
        


