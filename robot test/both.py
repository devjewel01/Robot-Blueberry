
#yes and no together
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)


time.sleep(1)
duty =2

while duty<=3.5:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty+0.5
    
time.sleep(2)

while duty>=0:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty-1
while duty>=0:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty-1
    
    
servo1.stop()
GPIO.cleanup()
print('done')
