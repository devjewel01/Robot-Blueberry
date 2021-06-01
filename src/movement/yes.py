from expression import *

singleTime = 0.08
doubleTime = 0.2
for loop in range(0,3):
    changeDegree([0],[10],singleTime,doubleTime)
    changeDegree([0],[45],singleTime,doubleTime)

changeDegree([0],[10],singleTime,doubleTime)
time.sleep(doubleTime)

