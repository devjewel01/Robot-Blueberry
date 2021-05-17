#!/usr/bin/env python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from googletrans import Translator
from gtts import gTTS
import requests
import os
import os.path
try:
    import RPi.GPIO as GPIO
except Exception as e:
    GPIO = None
import time
import re
import subprocess
import aftership
import json
import urllib.request
import pafy
import pprint
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))


with open('{}/src/config.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    configuration = yaml.load(conf, Loader=yaml.FullLoader)



if GPIO!=None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
else:
    GPIOcontrol=False

scriptname=configuration['Script']['scriptname']
scriptcommand=configuration['Script']['scriptcommand']


##Speech and translator declarations
translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
language='en-US'
translanguage=language.split('-')[0]
gender='Female'


#gTTS
def gttssay(phrase,saylang):
    tts = gTTS(text=phrase, lang=saylang)
    tts.save(femalettsfilename)
    os.system("mpg123 "+femalettsfilename)
    os.remove(femalettsfilename)

#Word translator
def trans(words,destlang,srclang):
    transword= translator.translate(words, dest=destlang, src=srclang)
    transword=transword.text
    transword=transword.replace("Text, ",'',1)
    transword=transword.strip()
    print(transword)
    return transword

#Text to speech converter with translation
def say(words,sourcelang=None,destinationlang=None):
    if sourcelang!=None and destinationlang!=None:
        sayword=trans(words,destinationlang,sourcelang)
        gttssay(sayword,translanguage)
    else:
        if sourcelang==None:
            sourcelanguage='en'
        else:
            sourcelanguage=sourcelang
        if sourcelanguage!=translanguage:
            sayword=trans(words,translanguage,sourcelanguage)
        else:
            sayword=words
        gttssay(sayword,translanguage,gender)


#Run scripts
def script(phrase):
    for num, name in enumerate(scriptname):
        if name.lower() in phrase:
            conv=scriptname[num]
            command=scriptcommand[num]
            print (command)
            say("Running " +conv)
            os.system(command)


#GPIO Device Control
def Action(phrase):
    print(phrase)
    if 'shutdown' in phrase:
        say('Shutting down Raspberry Pi')
        time.sleep(10)
        os.system("sudo shutdown -h now")
    elif 'hands up' in phrase:
        say('my hands up')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hands_up.py")
    elif 'hand up' in phrase:
        say('my hands up')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hands_up.py")
    elif 'hug me'  in phrase:
        say('come on and hug me')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hug.py")
    elif 'hath me'  in phrase:
        say('come on and hug me')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hug.py")
    elif 'hackme'  in phrase:
        say('come on and hug me')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hug.py")
    elif 'salute' in phrase:
        say('please take my salute')
        os.system("python3 /home/pi/Robot-Leena/robot-control/salute.py")
    elif 'hand shake' in phrase:
        say('hello I am leena')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hand_shake.py")
    elif 'handshake' in phrase:
        say('hello I am leena')
        os.system("python3 /home/pi/Robot-Leena/robot-control/hand_shake.py")
    elif 'move your hand' in phrase:
        say('see my hand movement')
        os.system("python3 /home/pi/Robot-Leena/robot-control/bothHand.py")
    elif 'movie hand' in phrase:
        say('see my hand movement')
        os.system("python3 /home/pi/Robot-Leena/robot-control/bothHand.py")
    elif 'move hand' in phrase:
        say('see my hand movement')
        os.system("python3 /home/pi/Robot-Leena/robot-control/bothHand.py")
    elif 'mop hand' in phrase:
        say('see my hand movement')
        os.system("python3 /home/pi/Robot-Leena/robot-control/bothHand.py")
    elif 'move your right hand' in phrase:
        say('my right hand')
        os.system("python3 /home/pi/Robot-Leena/robot-control/rightHand.py")
    elif 'move your left hand' in phrase:
        say('my left hand')
        os.system("python3 /home/pi/Robot-Leena/robot-control/leftHand.py")
    elif 'move your head' in phrase:
        say('I learn to move my head')
        os.system("python3 /home/pi/Robot-Leena/robot-control/yes.py")
        os.system("python3 /home/pi/Robot-Leena/robot-control/no.py")
    elif 'no' in phrase:
        say('I do not agree with you')
        os.system("python3 /home/pi/Robot-Leena/robot-control/no.py")
    elif 'yes' in phrase:
        say('I am agree with you')
        os.system("python3 /home/pi/Robot-Leena/robot-control/yes.py")
    elif 'left right' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/left-right.py")
    elif 'tata' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/tata.py")
    elif 'bye' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/bye.py")
    elif 'touch your head' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/touchHead.py")
    elif 'touch your nose' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/touchNose.py")
    elif 'touch your ear' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/touchEar.py")
    elif 'touch your eye' in phrase:
        os.system("python3 /home/pi/Robot-Leena/robot-control/touchEye.py")
    elif 'go forward' in phrase:
        say('go and go')
        os.system("python3 /home/pi/Robot-Leena/robot-control/goForward.py")
    elif 'go back'  in phrase:
        say('I do not like to go back')
        os.system("python3 /home/pi/Robot-Leena/robot-control/goBack.py")
    elif 'turn left' in phrase:
        say('turn left my face')
        os.system("python3 /home/pi/Robot-Leena/robot-control/turnLeft.py")
    elif 'tan lab' in phrase:
        say('turn left my face')
        os.system("python3 /home/pi/Robot-Leena/robot-control/turnLeft.py")
    elif 'turn right' in phrase:
        say('turn right my face')
        os.system("python3 /home/pi/Robot-Leena/robot-control/turnRight.py")
    elif 'turn write' in phrase:
        say('turn right my face')
        os.system("python3 /home/pi/Robot-Leena/robot-control/turnRight.py")
    else:
        say('please say the command again')