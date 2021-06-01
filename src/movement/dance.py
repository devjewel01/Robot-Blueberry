from expression import *

import multiprocessing

def pha():
    Run(1,0,1,0,50)
    time.sleep(2)

    Stop()
    Run(0,1,0,1,50)
    time.sleep(2)

    Stop()
    Run(0,1,1,0,100)
    time.sleep(0.5)

    Stop()
    Run(1,0,0,1,100)
    time.sleep(2)

    Stop()


def move():
    changeDegree([3,4,8,1,5,9,2,6,10,7,8],[80,120,50,80,40,180,110,120,20,100,80],0.01)
    for i in range(0,4):
       changeDegree([3,4],[100,80])
       changeDegree([7],[110])
       changeDegree([7],[90])
       changeDegree([8],[110])
       changeDegree([8],[90])
       changeDegree([5],[70])
       changeDegree([5],[100])
       changeDegree([6],[80])
       changeDegree([6],[120])
       changeDegree([1],[60])
       changeDegree([1],[80])
    takePosition()


def head():
    move_head(5)
    time.sleep(2)
    move_head(10)
    time.sleep(2)
    move_head(5)


def talk():
    say('ami banglai gan gai')
    time.sleep(0.5)
    say('amiii banglar gaan gaai')
    time.sleep(0.5)
    time.sleep('sobai amar gan sonteche')
    time.sleep(1)
    time.sleep('sobai ke donnobad')
    

p1 = multiprocessing.Process(target=talk,args=[])
p2 = multiprocessing.Process(target=move,args=[])
p3 = multiprocessing.Process(target=head,args=[])
p4 = multiprocessing.Process(target=pha,args=[])

if __name__ == '__main__':
    takePosition()
    p4.start()
    p2.start()
    p3.start()
    p1.start()
