import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
pin = 17
pin2 = 27
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
servo=GPIO.PWM(pin,50)
servo.start(2)

servo2=GPIO.PWM(pin2,50)
servo2.start(2)
time.sleep(1)


def takePosition():
    servo.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo.ChangeDutyCycle(2)
    time.sleep(0.5)
    
def takePositionSlow():
    servo2.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo2.ChangeDutyCycle(2)
    time.sleep(0.5)
        
def hug():
    takePosition()
    takePositionSlow()

def hands_up():
    takePosition()
    takePositionSlow()

def hand_shake():
    takePosition()
    #
    #
    takePositionSlow

def salute():
#salute
    takePosition()
    takePositionSlow()

def touch_head():
    takePosition()
    #
    #
    takePositionSlow()

def touch_nose():
    takePosition()
    #
    #
    takePositionSlow()

def touch_eye():
    takePosition()
    #
    #
    takePositionSlow()

def touch_ear():
    takePosition()
    #
    #
    takePositionSlow()

    




