# Useful debug
from time import time

START = 0
FINISH = 0
ACCUMULATOR = 0
DELTA = 0


def start():
    global START, DELTA
    START = time()
    DELTA = START


def finish():
    t = time()
    if ACCUMULATOR != 0:
        print "Acumulated time: {}".format(ACCUMULATOR)
    else:
        global FINISH
        FINISH = t
        print "Total time: {}".format(FINISH - START)


def accumulate():
    global ACCUMULATOR, DELTA
    t = time()
    ACCUMULATOR += t - DELTA
    DELTA = t
