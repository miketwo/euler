#!/usr/bin/env python
'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from itertools import count
from time import time

# multiple x * y for each x in 1-99, y=1-99
# check for palindromic number
# go from the top down (start at 99)
def main():
    num = 600851475143
    print "--- FACTORING {} ---".format(num)
    for prime in factor(num):
        print "PRIME: {}".format(prime)


if __name__ == '__main__':
    main()
