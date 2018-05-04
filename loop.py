# -*- coding: utf8 -*-
import time
import threading
import multiprocessing

def yes(no):
    while True: # 무한 루프를 도는 thread는 자신의 일을 끝내지 않는다.
        print "yes - %d\n" % no
        time.sleep(0.5) # 0.5초 쉬어라
        
def no(no):
    while True:
        print "no -%d\n" % no
        time.sleep(0.5)

# t1 = threading.Thread(target=yes, args=(1,)) # target(yes 함수)의 args(인자 갯수)가 한 개 이상
# t2 = threading.Thread(target=yes, args=(2,))

# 두 개를 각각 실행해라
# t1.start()
# t2.start()

if __name__ == '__main__': # python code를 import 되는 건지 독립적인 건지 몰라서
    p1 = multiprocessing.Process(target=yes, args=(1,))
    p2 = multiprocessing.Process(target=yes, args=(2,))
    p1.start()
    p2.start() # 실행시키면 하나의 프로세스에 대한 yes와 또 하나의 프로세스에 대한 yes가 겹친다. CPU에게 자원을 보장 받아서. 정말 동시수행. 