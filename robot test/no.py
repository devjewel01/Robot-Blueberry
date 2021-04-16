

import time
from adafruit_servokit import ServoKit

yes = ServoKit(channels=16)
yes.servo[1].angle = 90

time.sleep(0.5)
for i in range(90,180):
        yes.servo[1].angle = i
        time.sleep(0.05)

time.sleep(1)
for i in range(179,90,-1):
        yes.servo[1].angle = i
        time.sleep(0.05)

time.sleep(1)
for i in range(89,0,-1):
        yes.servo[1].angle = i
        time.sleep(0.05)
     
time.sleep(1)
for i in range(0,90):
        yes.servo[1].angle = i
        time.sleep(0.05)
        
print('done')

