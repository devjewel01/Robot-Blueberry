from expression import *

takePosition()

changeDegree([7,9,3,5,1],[60,0,60,180,50])
time.sleep(0.5)

for i in range(0,3):
    changeDegree([5],[160])
    changeDegree([5],[180])
    
time.sleep(1)
changeDegree([5,9,3,7,1],[170,60,0,180,50])

takePosition()
