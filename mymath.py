'''
Some math I made to help
'''
from math import ceil, sqrt
PRIMESET = set()  # Cache primes for faster retries


def prime_generator():
    yield 2
    yield 3
    num = 3
    while True:
        num += 2
        if is_prime(num):
            yield num


# A prime tester that should be faster on retries of the same number
def is_prime(num):
    global PRIMESET
    if num in PRIMESET:
        return True
    for i in xrange(2, int(ceil(sqrt(num))) + 1):
        if not num % i:
            return False
    PRIMESET.add(num)
    return True


# A BLAZINGLY-faster prime generator from the interwebs.
def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
