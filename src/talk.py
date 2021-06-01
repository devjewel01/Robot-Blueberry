#!/usr/bin/env python

from googletrans import Translator
from gtts import gTTS
import os
import os.path
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/src/conversation.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    custom_conversation = yaml.load(conf, Loader=yaml.FullLoader)

TTSChoice='GTTS'

translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
ttsfilename="/tmp/gcloud.mp3"
language='en-US'
translanguage=language.split('-')[0]
gender='Female'

def gttssay(phrase,saylang,specgender):
    tts = gTTS(text=phrase, lang=saylang)
    tts.save(femalettsfilename)
    os.system("mpg123 "+femalettsfilename)
    os.remove(femalettsfilename)


def trans(words,destlang,srclang):
    transword= translator.translate(words, dest=destlang, src=srclang)
    transword=transword.text
    transword=transword.replace("Text, ",'',1)
    transword=transword.strip()
    print(transword)
    return transword


def say(words,sourcelang=None,destinationlang=None):
    if sourcelang!=None and destinationlang!=None:
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
        gttssay(sayword,translanguage,gender)
