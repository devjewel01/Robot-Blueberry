import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1 = {'EN': 27, 'input1': 19, 'input2': 16}
Motor2 = {'EN': 22, 'input1': 26, 'input2': 20}

for x in Motor1:
    GPIO.setup(Motor1[x], GPIO.OUT)
    GPIO.setup(Motor2[x], GPIO.OUT)

EN1 = GPIO.PWM(Motor1['EN'], 100)    
EN2 = GPIO.PWM(Motor2['EN'], 100)    

EN1.start(0)                    
EN2.start(0)                    

for x in range(40, 100, 20):
    EN1.ChangeDutyCycle(x)
    EN2.ChangeDutyCycle(x)

    GPIO.output(Motor1['input1'], GPIO.HIGH)
    GPIO.output(Motor1['input2'], GPIO.LOW)
    
    GPIO.output(Motor2['input1'], GPIO.HIGH)
    GPIO.output(Motor2['input2'], GPIO.LOW)

    sleep(2)
    
                 

for x in range(100, 0, -20):
    EN1.ChangeDutyCycle(x)
    EN2.ChangeDutyCycle(x)

    GPIO.output(Motor1['input1'], GPIO.HIGH)
    GPIO.output(Motor1['input2'], GPIO.LOW)
    
    GPIO.output(Motor2['input1'], GPIO.HIGH)
    GPIO.output(Motor2['input2'], GPIO.LOW)

    sleep(1)
    
EN1.ChangeDutyCycle(0)
EN2.ChangeDutyCycle(0)

GPIO.cleanup()

