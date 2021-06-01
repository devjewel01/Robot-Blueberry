from expression import *

import multiprocessing

def talk():
    print('talk ')
    time.sleep(1)
    say("Hello This is robot Blueberry")

    say("I am from koomilla university")

    say("I made by quanta robotics team")

    say("Here's sanjit mondal is my circuit designer and mechanical designer")

    say("Jewel nath and mistu paul is my software developer")

    
def move():
    print('move')
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
    print('head wait for time')
    time.sleep(2)
    print('sleep time finished')
    for i in range(0,4):
        print('move head')
        yes(2);no(2);time.sleep(1)


p1 = multiprocessing.Process(target=talk,args=[])
p2 = multiprocessing.Process(target=move,args=[])
p3 = multiprocessing.Process(target=head,args=[])

if __name__ == '__main__':
    #takePosition()
    print('p2 start ')
    p1.start()
    p2.start()
    p3.start()
