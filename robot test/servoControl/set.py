import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
servo1=GPIO.PWM(7,50)
servo1.start(7)


time.sleep(1)
duty = 7

while duty<=12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty=duty+1
    
time.sleep(2)

while duty>=7:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty-1
    
    
servo1.stop()
GPIO.cleanup()
print('done')
