



import time
from adafruit_servokit import ServoKit

init  = [0,  20,  170, 180, 0, 10, 0, 0, 0, 0, 0, 0] 
limit = [35, 180, 0, 180, 140, 180, 180, 180, 180, 180, 180, 180]

h = ServoKit(channels=16)
def SetPosition :
	for i in range(0, 12):
		h.servo[i].angle = init[i]


while True:
	n = (int)(input("servo no : "))
	d = (int)(input("enter degree : "))
	h.servo[n].angle = d



print('done')
