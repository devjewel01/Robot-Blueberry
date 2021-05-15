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

while True:
    for x in range(40, 100):
        print ("FORWARD MOTION")
        EN1.ChangeDutyCycle(x)
        EN2.ChangeDutyCycle(x)

        GPIO.output(Motor1['input1'], GPIO.HIGH)
        GPIO.output(Motor1['input2'], GPIO.LOW)
        
        GPIO.output(Motor2['input1'], GPIO.HIGH)
        GPIO.output(Motor2['input2'], GPIO.LOW)

        sleep(0.1)
   
    print ("STOP")
    EN1.ChangeDutyCycle(0)
    EN2.ChangeDutyCycle(0)

    sleep(5)
     
    for x in range(40, 100):
        print ("BACKWARD MOTION")
        EN1.ChangeDutyCycle(x)
        EN2.ChangeDutyCycle(x)
        
        GPIO.output(Motor1['input1'], GPIO.LOW)
        GPIO.output(Motor1['input2'], GPIO.HIGH)

        GPIO.output(Motor2['input1'], GPIO.LOW)
        GPIO.output(Motor2['input2'], GPIO.HIGH)

        sleep(0.1)
     
    print ("STOP")
    EN1.ChangeDutyCycle(0)
    EN2.ChangeDutyCycle(0)

    sleep(5)

GPIO.cleanup()


