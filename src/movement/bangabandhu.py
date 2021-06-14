from expression import *
import multiprocessing

def talk():
    say("bangabandhu sheikh mujibur rahman is our father of nation.")
    say("he is the most hounarable person for our nation")
    p2.start()
    time.sleep(0.1)
    say("i salute him")
    time.sleep(1)
    say("i respect him from core of my heart")
    time.sleep(1.5)

def move():
    changeDegree([3,9,5],[100,0,130])
    changeDegree([7],[40])
    time.sleep(0.9)
    changeDegree([3,5,9], [70,60,90])
    changeDegree([7], [30])
    time.sleep(1.5)
    takePosition()
    

p2 = multiprocessing.Process(target=move,args=[])

talk()

