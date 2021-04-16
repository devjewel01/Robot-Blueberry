
import time
from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)

danfor = kit.servo[0]
bamfor = kit.servo[1]
yes = kit.servo[2]
no =  kit.servo[3]
danup = kit.servo[4]
bamup = kit.servo[5]

def NO():
	no.angle = 90
	while True:
		time.sleep(0.5)
		for i in range(90,180,5):
		        no.angle = i
		        time.sleep(0.05)

		time.sleep(1)
		for i in range(179,90,-5):
		        no.angle = i
		        time.sleep(0.05)
		time.sleep(1)


while True:
	time.sleep(1)
	danfor.angle = 0
	bamfor.angle = 180
	time.sleep(1)
	danfor.angle = 90
	bamfor.angle = 90     
	time.sleep(1)
	
	NO()
	
	time.sleep(1)      
	yes.angle = 35
	time.sleep(1)
	yes.angle = 0
	time.sleep(1)
	   
	danup.angle = 90
	bamup.angle = 90
	time.sleep(1)
	danup.angle = 0
	bamup.angle = 0
	time.sleep(1)
	danfor.angle = 0
	bamfor.angle = 180
	time.sleep(1)


