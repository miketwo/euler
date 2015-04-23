#!/usr/bin/env python
'''
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

from itertools import count
import debug


def check_number(num, maxdivisor):
    ''' Returns True/False if a number is divisible by all integers from 1 to
    maxdivisor. '''
    # This loop starts from the highest divisor and works back, because it's
    # more likely to return fast that way.
    for x in xrange(maxdivisor, 1, -1):
        if num % x:
            return False
    return True


# multiple x * y for each x in 1-99, y=1-99
# check for palindromic number
# go from the top down (start at 99)
def main():
    print "This should take about 10 seconds..."
    num = 20
    loopcounter = 0
    # We can start at num and increase by num because it has to be divisible
    # by num, so going through intermediate numbers wastes time.
    for i in count(num, num):
        loopcounter += 1
        if check_number(i, num):
            print i
            break


if __name__ == '__main__':
    main()
