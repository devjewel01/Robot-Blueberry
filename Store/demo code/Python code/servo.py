import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) #set board pin number 
#GPIO.setmode(GPIO.BCM) set GPIO pin number

GPIO.setup(11,GPIO.OUT)
servo=GPIO.PWM(11,50)
servo.start(0)
time.sleep(1)
duty =2

while duty<=12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty+1
    
time.sleep(1)


while duty>=0:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty-1
    
    
servo.stop()
GPIO.cleanup()
print('done')
