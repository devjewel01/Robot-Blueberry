import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')

engine.setProperty("voice", 'english_rp+f4')

def talk(text):  
    engine.say(text)
    engine.runAndWait()

talk("My name is robot leena")


