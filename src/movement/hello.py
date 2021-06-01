from expression import *

takePosition()
changeDegree([3],[60])
changeDegree([7],[140])
time.sleep(0.5)
#shake
speaking = ['hello','i','am','robot','blueberry']
GPIO.setup(21,GPIO.OUT)
head = GPIO.PWM(21,50)
head.start(0)
head.ChangeDutyCycle(2.5)
gttssay('hello i am robot blueberry','en','Female')
for i in range(0,5):    
    if i&1:
        changeDegree([7],[155])
        head.ChangeDutyCycle(4)
    else:
        changeDegree([7],[125])
        head.ChangeDutyCycle(3)
    time.sleep(0.2)
head.ChangeDutyCycle(2.5)
changeDegree([7],[140])
time.sleep(1)
#down
changeDegree([7],[180])
changeDegree([3],[0])
