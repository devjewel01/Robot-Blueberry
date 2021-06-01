from expression import *

import multiprocessing

def ff():
    changeDegree([3],[60])
    changeDegree([7],[140])
    time.sleep(0.5)

    #shake
    for i in range(0,5):    
        if i&1:
            changeDegree([7],[155])
        else:
            changeDegree([7],[125])
        time.sleep(0.2)
    changeDegree([7],[140])
    time.sleep(1)

    #down
    changeDegree([7],[180])
    changeDegree([3],[0])

def f():
    say('Hello I am robot Blueberry')


p1 = multiprocessing.Process(target=f, args=[])
p2 = multiprocessing.Process(target=ff, args=[])

if __name__ == '__main__':
    p1.start()
    p2.start()
    
