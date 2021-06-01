from expression import *

import multiprocessing
ok1=1;ok2=1
changeDegree([3,5,6,4],[20,40,140,140])
def Right():
    changeDegree([3,2],[20,0])
    #time.sleep(0.5)
    changeDegree([2,4],[130,50],0.01)
    #time.sleep(0.5)
def Left():
    changeDegree([4,1],[140,180])
    #time.sleep(0.5)
    changeDegree([1,3],[50,100],0.01)
    #time.sleep(0.5)

p1 = multiprocessing.Process(target=Right,args=[])
p2 = multiprocessing.Process(target=Left,args=[])
for i in range(0,4):
    Left()
    Right()
takePosition()
