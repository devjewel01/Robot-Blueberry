from expression import *


takePosition()
while True:
    print('pin & degree : ',end='')
    pin,deg = map(int, input().split())
    changeDegree([pin],[deg])
