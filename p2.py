#!/usr/bin/env python
'''
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2, the first 10 terms
will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''
from collections import deque

def fibonacci(maxnum):
    nums = deque(maxlen=2)
    nums.append(1)
    yield 1
    nums.append(2)
    yield 2
    while True:
        c = sum(nums)
        nums.append(c)
        if c < maxnum:
            yield c
        else:
            break

def main():
    total = 0
    i = 0
    for fib in fibonacci(4000000):
        i += 1
        if not fib%2:
            total += fib
            print "{:5}: {:10} -- {:10}".format(i,fib,total)
    print "---------------------"
    print total

if __name__ == '__main__':
    main()
