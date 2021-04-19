import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16) #define I2C

kit.servo[0].angle = 0  # Set angle 

time.sleep(1)

