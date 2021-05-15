import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

f = [10,9,25,11,8]
servo = [0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
for i in range(0,5):
    GPIO.setup(f[i],GPIO.OUT)
    servo[i] = GPIO.PWM(f[i],50)
    servo[i].start(0)
    
for i in range(0,5):
    servo[i].ChangeDutyCycle(3)
    time.sleep(0.05)
    servo[i].ChangeDutyCycle(6)
    time.sleep(0.05)
    servo[i].ChangeDutyCycle(9)
    time.sleep(0.05)
    servo[i].ChangeDutyCycle(12)
    time.sleep(2)

for i in range(0,5):
    servo[i].ChangeDutyCycle(0)
    

'''while True:
    for duty in range(0,12):
        for i in range(0,5):
            servo[i].ChangeDutyCycle(duty)
        time.sleep(0.1)
    for duty in range(12,0,-1):
        for i in range(0,5):
            servo[i].ChangeDutyCycle(duty)
        time.sleep(0.1)
    time.sleep(2)'''


GPIO.cleanup()
print('done')




