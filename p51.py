#!/usr/bin/env python
'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.



Method:
We generate a prime, generalize it to every permutation possible, then
create the families and check them. Caching results as we go speeds this up,
because there are tons of duplicates. We can also remove patterns that we know
don't produce primes, regardless of the other numbers.

Example:
Start with prime 103.
Generalized patterns for 3-digit #:
    (1) **n
    (2) *n*
    (3) n**
    (4) *nn
    (5) n*n
    (6) nn*
Remove patterns 2, 3, and 6. Because when the last digit is replaced with a
2, 5, or 0 it definitely won't be a prime. (Meaning the family will at most
have 7 primes.)
    (1) **n
    (4) *nn
    (5) n*n
Fill in the generalized patterns with nnn=103 to create families:
    (1) **n == **3 --> 113,223,333,443,553,663,773,883,993
    (4) *nn == *03 --> 103,203,303,403,503,603,703,803,903
    (5) n*n == 1*3 --> 103,113,123,133,143,153,163,173,183,193  (note that 0 can be substituted here)
Check each family for primes and count them:
    (1) 113 == True(prime), 223 == True, 333 == False(not prime), etc...
        5 of 9 are prime
    (4) 2 of 9 are prime
    (5) 5 of 10 are prime
Stop when a family of 8 are found.
Find the minimum number within that family.
'''
from math import sqrt, ceil
from itertools import permutations
import sys
import debug

PRIMESET = set()  # Cache primes for faster retries
COMBO_RESULTS = {}  # Cache results of family checking
PRIME_MASKS = {}  # Bucketed by number of digits in prime


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
    for i in xrange(2, int(ceil(sqrt(num)))+1):
        if not num % i:
            return False
    PRIMESET.add(num)
    return True


def generate_mask_for_num(num):
    '''
    Given nnn, generates 100, 010, 001, 110, 101, 011 for any size n.
    '''
    global PRIME_MASKS
    size = len(str(num))
    if size in PRIME_MASKS:
        return PRIME_MASKS[size]
    start = '0'*size
    # replace first x digits with 1, then permutate
    retval = set()
    for i in xrange(1, size):
        tmp = start.replace('0', '1', i)
        for p in permutations(tmp, size):
            retval.add(''.join(p))
    PRIME_MASKS[size] = retval
    return retval


def generate_combos_from_number(starting_num):
    '''
    ARGS
        starting_num - A number
    RETURNS
        A set of strings covering every possible combo of
        stars and digits. See examples
        Example: Given 13,  returns ('*3', '1*')
                 Given 103, returns ('10*', '1**', '*0*', '**3', '*03', '1*3')
    '''
    masks = generate_mask_for_num(starting_num)
    retval = set()
    for mask in masks:
        applied_mask = "".join(x if y != '1' else '*' for x, y in zip(str(starting_num), mask))
        retval.add(applied_mask)
    return retval


def generate_numbers_from_string_pattern(pattern):
    ''' Given a string of numbers and stars,
        generates number patterns by replacing the stars with 0-9.

    Example: Given 1*2, generates
             102,112,122,132,142,152,162,172,182,192

    Notes: Leading stars do NOT get 0.
           *n --> 1n,2n,3n...9n -- but not 0n
    '''
    retval = set()
    for i in xrange(10):
        # Skip leading 0's
        if pattern[0] == "*" and i == 0:
            continue
        temp = pattern.replace('*', str(i))
        retval.add(int(temp))
    return retval


def return_amount_of_primes_in_a_list(numbers):
    return sum([is_prime(number) for number in numbers])


def return_true_if_at_least_x_primes_in_list(numbers, min_primes):
    counter = 0
    list_size = len(numbers)
    maxfails = list_size - min_primes
    for num in numbers:
        if not is_prime(num):
            counter += 1
        if counter >= maxfails:
            return False
    return True


def main():
    for prime in prime_generator():
        if len(str(prime)) < 2:
            continue
        combos = generate_combos_from_number(prime)
        # Remove ones with stars in the last digit. They will not be primes
        # when a 2 is substituted.
        combos = filter(lambda x: x[-1] != "*", combos)
        comboloopcount = 0
        for combo in combos:
            if combo in COMBO_RESULTS:
                continue
            comboloopcount += 1
            numbers = generate_numbers_from_string_pattern(combo)
            tf = return_true_if_at_least_x_primes_in_list(numbers, 7)
            COMBO_RESULTS[combo] = tf
            if tf:
                total = return_amount_of_primes_in_a_list(numbers)
                # print "Prime {}: Combo {}: {} of 10 are prime".format(prime, comboloopcount, total)
                if total == 8:
                    print "GOT IT!"
                    print combo
                    print numbers
                    print min(numbers)
                    debug.finish()
                    sys.exit()


def runtests():
    expected = set(('*3', '1*'))
    result = generate_combos_from_number(13)
    assert expected == result, "{} != {}".format(expected, result)

    expected = set(('8*', '*7'))
    result = generate_combos_from_number(87)
    assert expected == result, "{} != {}".format(expected, result)

    expected = set(('1*', '*1'))
    result = generate_combos_from_number(11)
    assert expected == result, "{} != {}".format(expected, result)

    expected = set(('10*', '1*3', '*03', '1**', '**3', '*0*'))
    result = generate_combos_from_number(103)
    assert expected == result, "{} != {}".format(expected, result)

    expected = set((13,23,33,43,53,63,73,83,93))
    result = generate_numbers_from_string_pattern('*3')
    assert expected == result, "{} != {}".format(expected, result)

    expected = set((10,11,12,13,14,15,16,17,18,19))
    result = generate_numbers_from_string_pattern('1*')
    assert expected == result, "{} != {}".format(expected, result)

    expected = set((103,113,123,133,143,153,163,173,183,193))
    result = generate_numbers_from_string_pattern('1*3')
    assert expected == result, "{} != {}".format(expected, result)

    expected = set((113,223,333,443,553,663,773,883,993))
    result = generate_numbers_from_string_pattern('**3')
    assert expected == result, "{} != {}".format(expected, result)

    expected = set(('100', '010', '001', '110', '101', '011'))
    result = generate_mask_for_num(123)
    assert expected == result, "{} != {}".format(expected, result)

    # Quick speed tests
    print "Timing generate_combos_from_number"
    debug.start()
    for i in range(10000):
        generate_combos_from_number(12345)
    debug.finish()

    print "Timing prime_generator"
    debug.start()
    p = 2
    while p < 1000000:
        p = prime_generator()
    debug.finish()


if __name__ == '__main__':
    main()

