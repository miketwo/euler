# Useful debug
'''
Author: Michael Ricks-Aherne

This file contains a bunch of useful timing functions for profiling code.
They are not as extensive or accurate as Python's timeit or profiler, but are
meant to be used quickly for a rough estimate.
'''
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


# Recipe from http://code.activestate.com/recipes/578776-a-simple-timing-function/
# Modified slightly for more accuracy
def dur(op=None, clock=[time()]):
    t = time()
    if op is not None:
        duration = t - clock[0]
        print '%s finished. Duration %.6f seconds.' % (op, duration)
    clock[0] = t
