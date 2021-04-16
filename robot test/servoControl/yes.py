import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(2)

GPIO.setup(7,GPIO.OUT)
servo2=GPIO.PWM(7,50)
servo2.start(2)

time.sleep(1)
d1 = 2
d2 = 7

while d2<=12:
    servo1.ChangeDutyCycle(d2)
    time.sleep(0.1)
    d2=d2+1    
time.sleep(2)
while d2>=7:
    servo1.ChangeDutyCycle(d2)
    time.sleep(0.05)
    d2=d2-1
time.sleep(2)
while d2>=7:
    servo1.ChangeDutyCycle(d2)
    time.sleep(0.05)
    d2=d2-1
  
while d1<=3.5:
    servo1.ChangeDutyCycle(d1)
    time.sleep(0.05)
    d1=d1+0.5    
time.sleep(2)
while d1>=0:
    servo1.ChangeDutyCycle(d1)
    time.sleep(0.05)
    d1=d1-0.5 
    
servo1.stop()
servo2.stop()
GPIO.cleanup()
print('done')
