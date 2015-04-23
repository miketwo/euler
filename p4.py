#!/usr/bin/env python
'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from itertools import count
from time import time

# multiple x * y for each x in 1-99, y=1-99
# check for palindromic number
# go from the top down (start at 99)


def main():
    top = 999
    bottom = 100
    biggest = 0
    for x in xrange(top, bottom, -1):
        for y in xrange(top, bottom, -1):
            res = x * y
            if res > biggest:
                if str(res) == str(res)[::-1]:
                    biggest = res
                    print "{} * {} = {}".format(x, y, res)


if __name__ == '__main__':
    main()
