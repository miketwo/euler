#!/usr/bin/env python
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import mymath


def main():
    primes = mymath.rwh_primes2(2000000)
    print "Sum = {}".format(sum(primes))

if __name__ == '__main__':
    main()
