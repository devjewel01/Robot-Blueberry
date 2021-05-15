

import time
from adafruit_servokit import ServoKit

yes = ServoKit(channels=16)
yes.servo[0].angle = 0
time.sleep(0.5)
for i in range(0,35):
        yes.servo[0].angle = i
        time.sleep(0.5)

time.sleep(0.5)
for i in range(34,0,-1):
        yes.servo[0].angle = i
        time.sleep(0.5)

print('done')

