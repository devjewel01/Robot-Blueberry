from expression import *
from threading import Thread

def song():
    changeDegree([3,5,9], [70,60,90])
    changeDegree([7], [30])
    os.system('aplay /home/pi/Robot-Blueberry/audio-files/national-song.wav')
    takePosition()

def move():
    time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=song)
    t2 = Thread(target=move)
    t1.start()
    t2.start()
