from expression import *

takePosition()
changeDegree([5,9,6,10],[40,180,120,20])
changeDegree([3,4],[60,120])
#changeDegree([7,8],[100,80])
list = ['dul','dul','duloni', 'ranga','mathay']
for i in range(0,5):
    changeDegree([1,2,7,8],[10,100,90,80])
    time.sleep(0.05)
    say(list[i])
    changeDegree([1,2,7,8],[80,150,120,110])
    time.sleep(0.05)
changeDegree([1,2],[50,130])
changeDegree([7,8,5,6,9,10],[180,0,Initial[5],Initial[6],Initial[9],Initial[10]])
changeDegree([3,4],[0,180])

takePosition()
'''
5,9,6,10 40,180,120,20
7,8 140 120

'''
