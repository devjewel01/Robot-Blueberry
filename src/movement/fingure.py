from expression import *

takePosition()
changeDegree([4,6,10],[120,0,50])
deg1 = [0,0,0,180,180,180]
deg2 = [0,180,180,0,0,0]
for i in range(0,3):
    for f in range(1,6):
        changeDegreeGpio([f],[90],20,0.01)
        time.sleep(1)
        changeDegreeGpio([f],[deg2[f]],20,0.01)
        time.sleep(1)
    for f in range(1,6):
        changeDegreeGpio([f],[deg1[f]],20,0.01)
        time.sleep(1)
        changeDegreeGpio([f],[deg2[f]],20,0.01)
        time.sleep(1)
    print('now ',i)
        
takePosition()
