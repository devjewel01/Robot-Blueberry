from servo import *

takePosition()
changeDegree([5,9,3,1],[70,180,180,90])
changeDegree([7],[60])
time.sleep(1)

changeDegree([7],[180])
changeDegree([3,1,5,9],[0,50,Initial[5],Initial[9]])
takePosition()


