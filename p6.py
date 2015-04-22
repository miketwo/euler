#!/usr/bin/env python
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the
squares of the first ten natural numbers and the square of the sum is 3025 -
385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

from itertools import count
import debug

def sum_square(maxnum):
    total = 0
    for i in xrange(1, maxnum+1):
        total += i**2
    return total

def square_sum(maxnum):
    total = 0
    for i in xrange(1, maxnum+1):
        total += i
    return total**2

def main():
    num = 100
    a = sum_square(num)
    b = square_sum(num)
    c = b - a
    print "{}, {}, {}".format(a,b,c)


if __name__ == '__main__':
    main()

