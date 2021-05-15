import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

f = [10,9,25,11,8]
servo = [0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
for i in range(0,5):
    GPIO.setup(f[i],GPIO.OUT)
    servo[i] = GPIO.PWM(f[i],50)
    if(i<3):
        servo[i].start(0)
    else:
        servo[i].start(12)
while True:
    for duty in range(0,12):
        for i in range(0,5):
            if(i<3):
                servo[i].ChangeDutyCycle(duty)
            else:
                servo[i].ChangeDutyCycle(12-duty)
        time.sleep(0.1)
        
    for duty in range(12,0,-1):
        for i in range(0,5):
            if(i<3):
                servo[i].ChangeDutyCycle(duty)
            else:
                servo[i].ChangeDutyCycle(12-duty)
        time.sleep(0.1)
        
    time.sleep(2)


GPIO.cleanup()
print('done')



