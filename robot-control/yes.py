import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) 

GPIO.setup(21,GPIO.OUT)
servo=GPIO.PWM(21,50)
servo.start(0)
duty = 0

while duty<=5:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.08)
    duty=duty+0.1
    
time.sleep(1)


while duty>=0:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.08)
    duty=duty-0.1
    
    
servo.stop()
GPIO.cleanup()


