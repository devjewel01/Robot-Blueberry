from expression import *

takePosition()

#start
changeDegree([3,4],[100,70])
changeDegree([1,2],[170,10])
changeDegree([7,8],[70,120])
changeDegree([5,9,6,10],[90,180,80,30])
time.sleep(2)

#stop
changeDegree([5,9,6,10],[170,60,0,150])
changeDegree([7,8],[170,0])
changeDegree([1,2],[50,130])
changeDegree([3,4],[0,170])

takePosition()
