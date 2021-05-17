#!/usr/bin/env python

from __future__ import print_function
import faulthandler
faulthandler.enable()

try:
    import RPi.GPIO as GPIO
except Exception as e:
    GPIO = None
    
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from actions import say
from actions import trans
from actions import Action
from actions import script

from actions import configuration
from threading import Thread
from pathlib import Path

from actions import gender
from actions import translanguage
from actions import language
from audiorecorder import record_to_file

import argparse
import json
import os.path
import pathlib2 as pathlib
import os
import struct
import subprocess
import re
import psutil
import logging
import time
import random


import numpy as np
import pvporcupine
import pyaudio
import soundfile

import sys
import signal
import requests
import io
import google.oauth2.credentials
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
from google.assistant.library.device_helpers import register_device
if GPIO!=None:
    from indicator import assistantindicator
    from indicator import stoppushbutton
    GPIOcontrol=True
else:
    GPIOcontrol=False

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

WARNING_NOT_REGISTERED = ""


if os.path.isfile('/tmp/robot.log'):
    os.system('sudo rm /tmp/robot.log')

logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG , filename='/tmp/robot.log')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))



mutestopbutton=True

if configuration['Wakewords']['Custom_Wakeword']=='Enabled':
    custom_wakeword=True
else:
    custom_wakeword=False


picovoice_models=configuration['Wakewords']['Picovoice_wakeword_models']

if configuration['Wakewords']['Wakeword_Engine']=='Picovoice':
    wakeword_length=len(picovoice_models)


numques=len(configuration['Conversation']['question'])
numans=len(configuration['Conversation']['answer'])

class Myassistant():

    def __init__(self):
        self.interrupted=False
        self.can_start_conversation=False
        self.assistant=None
        self._library_path = pvporcupine.LIBRARY_PATH
        self._model_path = pvporcupine.MODEL_PATH
        self._keyword_paths = picovoice_models
        self._input_device_index = None
        self._sensitivities = [0.5]*wakeword_length

        self.mutestatus=False
        self.interpreter=False
        self.interpconvcounter=0
        self.interpcloudlang1=language
        self.interpttslang1=translanguage
        self.interpcloudlang2=''
        self.interpttslang2=''
        self.singleresposne=False
        self.singledetectedresponse=''

        if configuration['Wakewords']['Wakeword_Engine']=='Picovoice':
            self.t1 = Thread(target=self.picovoice_run)
        if GPIOcontrol:
            self.t2 = Thread(target=self.pushbutton)

    def signal_handler(self,signal, frame):
        self.interrupted = True

    def interrupt_callback(self,):
        return self.interrupted

    def buttonsinglepress(self):
        if os.path.isfile("{}/.mute".format(USER_PATH)):
            os.system("sudo rm {}/.mute".format(USER_PATH))
            assistantindicator('unmute')
            if configuration['Wakewords']['Ok_Google']=='Disabled':
                self.assistant.set_mic_mute(True)
                print("Mic is open, but Ok-Google is disabled")
            else:
                self.assistant.set_mic_mute(False)
            # if custom_wakeword:
            #     self.t1.start()
                print("Turning on the microphone")
        else:
            open('{}/.mute'.format(USER_PATH), 'a').close()
            assistantindicator('mute')
            self.assistant.set_mic_mute(True)
            # if custom_wakeword:
            #     self.thread_end(t1)
            print("Turning off the microphone")

    def buttondoublepress(self):
        print('Stopped')
        stop()

    def pushbutton(self):
        if GPIOcontrol:
            while mutestopbutton:
                time.sleep(.1)
                if GPIO.event_detected(stoppushbutton):
                    GPIO.remove_event_detect(stoppushbutton)
                    now = time.time()
                    count = 1
                    GPIO.add_event_detect(stoppushbutton,GPIO.RISING)
                    while time.time() < now + 1:
                         if GPIO.event_detected(stoppushbutton):
                             count +=1
                             time.sleep(.25)
                    if count == 2:
                        self.buttonsinglepress()
                        GPIO.remove_event_detect(stoppushbutton)
                        GPIO.add_event_detect(stoppushbutton,GPIO.FALLING)
                    elif count == 3:
                        self.buttondoublepress()
                        GPIO.remove_event_detect(stoppushbutton)
                        GPIO.add_event_detect(stoppushbutton,GPIO.FALLING)

    def process_device_actions(self,event, device_id):
        if 'inputs' in event.args:
            for i in event.args['inputs']:
                if i['intent'] == 'action.devices.EXECUTE':
                    for c in i['payload']['commands']:
                        for device in c['devices']:
                            if device['id'] == device_id:
                                if 'execution' in c:
                                    for e in c['execution']:
                                        if 'params' in e:
                                            yield e['command'], e['params']
                                        else:
                                            yield e['command'], None


    def process_event(self,event):
        print(event)
        print()
        if event.type == EventType.ON_MUTED_CHANGED:
            self.mutestatus=event.args["is_muted"]

        if event.type == EventType.ON_START_FINISHED:
            self.can_start_conversation = True
            if GPIOcontrol:
                self.t2.start()
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                assistantindicator('mute')
            if (configuration['Wakewords']['Ok_Google']=='Disabled' or os.path.isfile("{}/.mute".format(USER_PATH))):
                self.assistant.set_mic_mute(True)
            if custom_wakeword:
                self.t1.start()


        if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
            subprocess.Popen(["aplay", "{}/audio-files/Fb.wav".format(ROOT_PATH)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.can_start_conversation = False
            if GPIOcontrol:
                assistantindicator('listening')

        if (event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT or event.type == EventType.ON_NO_RESPONSE):
            self.can_start_conversation = True
            if GPIOcontrol:
                assistantindicator('off')

            if (configuration['Wakewords']['Ok_Google']=='Disabled' or os.path.isfile("{}/.mute".format(USER_PATH))):
                  self.assistant.set_mic_mute(True)
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                if GPIOcontrol:
                    assistantindicator('mute')


        if (event.type == EventType.ON_RESPONDING_STARTED and event.args and not event.args['is_error_response']):
            if GPIOcontrol:
                assistantindicator('speaking')

        if event.type == EventType.ON_RESPONDING_FINISHED:
            if GPIOcontrol:
                assistantindicator('off')

        if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
            if GPIOcontrol:
                assistantindicator('off')
            if self.singleresposne:
                self.assistant.stop_conversation()
                self.singledetectedresponse= event.args["text"]
            else:
                usrcmd=event.args["text"]
                self.custom_command(usrcmd)

        if event.type == EventType.ON_RENDER_RESPONSE:
            if GPIOcontrol:
                assistantindicator('off')
            

        if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
                event.args and not event.args['with_follow_on_turn']):
            self.can_start_conversation = True
            if GPIOcontrol:
                assistantindicator('off')
            if (configuration['Wakewords']['Ok_Google']=='Disabled' or os.path.isfile("{}/.mute".format(USER_PATH))):
                self.assistant.set_mic_mute(True)
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                if GPIOcontrol:
                    assistantindicator('mute')


        if event.type == EventType.ON_DEVICE_ACTION:
            for command, params in event.actions:
                print('Do command', command, 'with params', str(params))


    def register_device(self,project_id, credentials, device_model_id, device_id):
        base_url = '/'.join([DEVICE_API_URL, 'projects', project_id, 'devices'])
        device_url = '/'.join([base_url, device_id])
        session = google.auth.transport.requests.AuthorizedSession(credentials)
        r = session.get(device_url)
        print(device_url, r.status_code)
        if r.status_code == 404:
            print('Registering....')
            r = session.post(base_url, data=json.dumps({
                'id': device_id,
                'model_id': device_model_id,
                'client_type': 'SDK_LIBRARY'
            }))
            if r.status_code != 200:
                raise Exception('failed to register device: ' + r.text)
            print('\rDevice registered.')


    def detected(self):
        if self.can_start_conversation == True:
            if self.mutestatus:
                self.assistant.set_mic_mute(False)
                time.sleep(1)
                self.assistant.start_conversation()
            if not self.mutestatus:
                self.assistant.start_conversation()
            print('Assistant is listening....')

    def start_detector(self):
        self.detector.start(detected_callback=self.callbacks,
            interrupt_check=self.interrupt_callback,
            sleep_time=0.03)

    def picovoice_run(self):
        keywords = list()
        for x in self._keyword_paths:
            keywords.append(os.path.basename(x).replace('.ppn', '').split('_')[0])

        porcupine = None
        pa = None
        audio_stream = None
        try:
            porcupine = pvporcupine.create(
                library_path=self._library_path,
                model_path=self._model_path,
                keyword_paths=self._keyword_paths,
                sensitivities=self._sensitivities)

            pa = pyaudio.PyAudio()

            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length,
                input_device_index=self._input_device_index)

            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                result = porcupine.process(pcm)
                if result >= 0:
                    self.detected()

        except KeyboardInterrupt:
            print('Stopping ...')
        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()

    def voicenote_recording(self):
        recordfilepath='/tmp/audiorecord.wav'
        subprocess.Popen(["aplay", "{}/audio-files/Fb.wav".format(ROOT_PATH)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while not record_to_file(recordfilepath):
            time.sleep(.1)
        voicenote(recordfilepath)

    def single_user_response(self,prompt):
        self.singledetectedresponse=''
        self.singleresposne=True
        say(prompt)
        self.assistant.start_conversation()
        while self.singledetectedresponse=='':
            time.sleep(.1)
        self.singleresposne=False
        return self.singledetectedresponse

    def custom_command(self,usrcmd):
        if configuration['Script']['Script_Control']=='Enabled':
            if 'script'.lower() in str(usrcmd).lower():
                script(str(usrcmd).lower())

        
                    
        if configuration['Conversation']['Conversation_Control']=='Enabled':
            for i in range(1,numques+1):
                try:
                    if str(configuration['Conversation']['question'][i][0]).lower() in str(usrcmd).lower():
                        self.assistant.stop_conversation()
                        selectedans=random.sample(configuration['Conversation']['answer'][i],1)
                        say(selectedans[0])
                        break
                except Keyerror:
                    say('Please check if the number of questions matches the number of answers')
                    
                    

        if configuration['Raspberrypi_GPIO_Control']['GPIO_Control']=='Enabled':
            if 'robot'.lower() in str(usrcmd).lower():
                self.assistant.stop_conversation()
                command = str(usrcmd).lower()
                command = command.replace('robot', '')
                Action(command)



    def main(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--device-model-id', '--device_model_id', type=str,
                            metavar='DEVICE_MODEL_ID', required=False,
                            help='the device model ID registered with Google')
        parser.add_argument('--project-id', '--project_id', type=str,
                            metavar='PROJECT_ID', required=False,
                            help='the project ID used to register this device')
        parser.add_argument('--nickname', type=str,
                        metavar='NICKNAME', required=False,
                        help='the nickname used to register this device')
        parser.add_argument('--device-config', type=str,
                            metavar='DEVICE_CONFIG_FILE',
                            default=os.path.join(
                                os.path.expanduser('~/.config'),
                                'googlesamples-assistant',
                                'device_config_library.json'
                            ),
                            help='path to store and read device configuration')
        parser.add_argument('--credentials', type=existing_file,
                            metavar='OAUTH2_CREDENTIALS_FILE',
                            default=os.path.join(
                                os.path.expanduser('~/.config'),
                                'google-oauthlib-tool',
                                'credentials.json'
                            ),
                            help='path to store and read OAuth2 credentials')
        parser.add_argument('--query', type=str,
                        metavar='QUERY',
                        help='query to send as soon as the Assistant starts')
        parser.add_argument('-v', '--version', action='version',
                            version='%(prog)s ' + Assistant.__version_str__())

        args = parser.parse_args()
        with open(args.credentials, 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None,
                                                                **json.load(f))

        device_model_id = None
        last_device_id = None
        try:
            with open(args.device_config) as f:
                device_config = json.load(f)
                device_model_id = device_config['model_id']
                last_device_id = device_config.get('last_device_id', None)
        except FileNotFoundError:
            pass

        if not args.device_model_id and not device_model_id:
            raise Exception('Missing --device-model-id option')

        should_register = (
            args.device_model_id and args.device_model_id != device_model_id)

        device_model_id = args.device_model_id or device_model_id
        with Assistant(credentials, device_model_id) as assistant:
            self.assistant = assistant
            subprocess.Popen(["aplay", "/home/pi/Robot-Leena/audio-files/welcome leena.wav".format(ROOT_PATH)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            events = assistant.start()
            device_id = assistant.device_id
            print('device_model_id:', device_model_id)
            print('device_id:', device_id + '\n')

            # Re-register if "device_id" is different from the last "device_id":
            if should_register or (device_id != last_device_id):
                if args.project_id:
                    register_device(args.project_id, credentials,
                                    device_model_id, device_id, args.nickname)
                    pathlib.Path(os.path.dirname(args.device_config)).mkdir(
                        exist_ok=True)
                    with open(args.device_config, 'w') as f:
                        json.dump({
                            'last_device_id': device_id,
                            'model_id': device_model_id,
                        }, f)
                else:
                    print(WARNING_NOT_REGISTERED)

            for event in events:
                if event.type == EventType.ON_START_FINISHED and args.query:
                    assistant.send_text_query(args.query)
                self.process_event(event)

        if custom_wakeword:
            self.detector.terminate()


if __name__ == '__main__':
    try:
        Myassistant().main()
    except Exception as error:
        logging.exception(error)

