"""
Synopsis:
    Create 10 threads.
    Each thread does the following:
        1. Increment a global count and prints it.
        2. Sleeps (waits) for 3 seconds.
        3. Prints the global count and decrements it.
Usage:
    python simple_threads.py
"""

import time
from threading import Thread, Lock

Count = 0
Singlelock = Lock()


def myfunc(threadno):
    global Count
    Singlelock.acquire()
    Count += 1
    print "sleeping 3 sec from thread %d  Count %d" % (threadno, Count, )
    Singlelock.release()
    time.sleep(3)
    Singlelock.acquire()
    print "finished sleeping from thread %d  Count %d" % (threadno, Count, )
    Count -= 1
    Singlelock.release()


def test():
    for threadno in range(10):
        t = Thread(target=myfunc, args=(threadno,))
        t.start()


test()
