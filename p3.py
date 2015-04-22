#!/usr/bin/env python
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from itertools import count
from time import time

# Prints all primes for a given number.
# Uses recursion
def factor(number):
    # Divide the number by every prime lower than it.
    # it it divides evenly, do it again with the remainder.
    # if not, move on to the next prime.
    # if no division is found, it's a prime number.
    for i in count(start=2, step=1):
        division, remainder = divmod(number, i)
        # print "{}/{} = {} R{}".format(number, i, division, remainder)
        if not remainder:
            yield i
            # Wacky recursive yield
            for r in factor(division):
                yield r
            raise StopIteration
        if i >= number:
            raise StopIteration
    yield number


def main():
    num = 600851475143
    print "--- FACTORING {} ---".format(num)
    for prime in factor(num):
        print "PRIME: {}".format(prime)


if __name__ == '__main__':
    main()
