# Useful debug
from time import time

START = 0
FINISH = 0

def start():
    global START
    START = time()

def finish():
    global FINISH
    FINISH = time()
    print FINISH - START
