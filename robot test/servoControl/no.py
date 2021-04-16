import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
servo=GPIO.PWM(7,50)
servo.start(7)


servo.ChangeDutyCycle(2)
time.sleep(2)
servo.ChangeDutyCycle(12)
time.sleep(1)
    
    
servo1.stop()
GPIO.cleanup()
print('done')
