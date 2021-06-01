from expression import *

times=2
Run(1,0,1,0,100)
while times>=0:
    changeDegree([3,4],[70,170])
    time.sleep(0.05)
    changeDegree([3,4],[0,100])
    time.sleep(0.05)
    times-=1
takePosition()
Stop_Slow(1,0,1,0)
