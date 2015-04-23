#!/usr/bin/env python
'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from math import sqrt, ceil


def prime_generator():
    yield 2
    yield 3
    num = 3
    while True:
        num += 2
        if is_prime(num):
            yield num


def is_prime(num):
    for i in xrange(2, int(ceil(sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True


def main():
    print is_prime(9)
    loop = 0
    for prime in prime_generator():
        loop += 1
        print "{}: {}".format(loop, prime)
        if loop == 10001:
            break


if __name__ == '__main__':
    main()
