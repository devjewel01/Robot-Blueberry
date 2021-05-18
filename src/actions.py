#!/usr/bin/env python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from googletrans import Translator
from google.cloud import texttospeech
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
import feedparser
import json
import urllib.request
import pafy
import pprint
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))


with open('{}/src/config.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    configuration = yaml.load(conf, Loader=yaml.FullLoader)


TTSChoice=''
if configuration['TextToSpeech']['Choice']=="Google Cloud":
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        if configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']!="ENTER THE PATH TO YOUR TTS CREDENTIALS FILE HERE":
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = configuration['TextToSpeech']['Google_Cloud_TTS_Credentials_Path']
            TTSChoice='GoogleCloud'
            client = texttospeech.TextToSpeechClient()
        else:
            print("Set the path to your Google cloud text to speech credentials in the config.yaml file. Using gTTS for now.....")
            TTSChoice='GTTS'
    else:
        TTSChoice='GoogleCloud'
        client = texttospeech.TextToSpeechClient()
else:
    TTSChoice='GTTS'



if GPIO!=None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Number of entities in 'var' and 'PINS' should be the same
    var = configuration['Raspberrypi_GPIO_Control']['lightnames']
    '''gpio = configuration['Gpios']['picontrol']
    for pin in gpio:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)'''

    #Servo pin declaration
    '''servopin=configuration['Gpios']['servo'][0]
    GPIO.setup(servopin, GPIO.OUT)
    pwm=GPIO.PWM(servopin, 50)
    pwm.start(0)'''

    #Stopbutton
    '''stoppushbutton=configuration['Gpios']['stopbutton_music_AIY_pushbutton'][0]
    GPIO.setup(stoppushbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIOcontrol=True'''
else:
    GPIOcontrol=False

#Number of scripts and script names should be the same
scriptname=configuration['Script']['scriptname']
scriptcommand=configuration['Script']['scriptcommand']



##Speech and translator declarations
translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
malettsfilename="/tmp/male-say.wav"
ttsfilename="/tmp/gcloud.mp3"
language=configuration['Language']['Choice']
translanguage=language.split('-')[0]
gender=''
if configuration['TextToSpeech']['Voice_Gender']=='Male':
    gender='Male'
elif configuration['TextToSpeech']['Voice_Gender']=='Female':
    gender='Female'
else:
    gender='Female'



#gTTS
def gttssay(phrase,saylang,specgender):
    tts = gTTS(text=phrase, lang=saylang)
    tts.save(femalettsfilename)
    if specgender=='Male':
        os.system('sox ' + femalettsfilename + ' ' + malettsfilename + ' pitch -450')
        os.remove(femalettsfilename)
        os.system('aplay ' + malettsfilename)
        os.remove(malettsfilename)
    elif specgender=='Female':
        os.system("mpg123 "+femalettsfilename)
        os.remove(femalettsfilename)

#Google Cloud Text to Speech
def gcloudsay(phrase,lang):
    try:
        if gender=='Male':
            gcloudgender=texttospeech.enums.SsmlVoiceGender.MALE
        else:
            gcloudgender=texttospeech.enums.SsmlVoiceGender.FEMALE

        synthesis_input = texttospeech.types.SynthesisInput(text=phrase)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code=lang,
            ssml_gender=gcloudgender)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(ttsfilename, 'wb') as out:
            out.write(response.audio_content)
        if gender=='Male' and lang=='it-IT':
            os.system('sox ' + ttsfilename + ' ' + malettsfilename + ' pitch -450')
            os.remove(ttsfilename)
            os.system('aplay ' + malettsfilename)
            os.remove(malettsfilename)
        else:
            os.system("mpg123 "+ttsfilename)
            os.remove(ttsfilename)
    except google.api_core.exceptions.ResourceExhausted:
        print("Google cloud text to speech quota exhausted. Using GTTS. Make sure to change the choice in config.yaml")
        gttssay(phrase,lang)

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
        if TTSChoice=='GoogleCloud':
            sayword=trans(words,destinationlang,sourcelang)
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
            sayword=trans(words,destinationlang,sourcelang)
            gttssay(sayword,translanguage,gender)
    else:
        if sourcelang==None:
            sourcelanguage='en'
        else:
            sourcelanguage=sourcelang
        if sourcelanguage!=translanguage:
            sayword=trans(words,translanguage,sourcelanguage)
        else:
            sayword=words
        if TTSChoice=='GoogleCloud':
            gcloudsay(sayword,language)
        elif TTSChoice=='GTTS':
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


#Stepper Motor control
def SetAngle(angle):
    if GPIOcontrol:
        duty = angle/18 + 2
        GPIO.output(servopin, True)
        say("Moving motor by " + str(angle) + " degrees")
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        pwm.ChangeDutyCycle(0)
        GPIO.output(servopin, False)
    else:
        say("GPIO controls, is not supported for your device.")


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

