#!/usr/bin/env python
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
------

Interesting.
a^2 + b^2 = c^2, where a < b < c, and a + b + c = 1000.
I feel like this could almost be solved on paper.
Assume positive integers only.

If a + b + c = 1000, that means a + b = 1000 - c. So I only need to pick a and
b, c will be set. If a < b < c, it means that, for any given a, b ranges from
a+1 to 1000-a+2.

How? See this example:
Assume a = 20.
The smallest b is 21, because a < b. Another way of writing that is a + 1.
Because they're on opposite sides of the equation, as b increases,
c descreases, and vice-versa. So the LARGEST b happens at the smallest c.
The smallest c needs to be 1 greater than b. So it's b + 1. Or, since b is
a + 1, the smallest c is a + 2.
When c is a + 2, b must be 1000 - a + 2.
So the range of b is:
    a + 1   to   1000-a+2
We'll brute force over that loop, checking for an exit condition.
'''


def main():
    loops = 0
    for a in range(1, 1000):
        for b in range(a+1, 1000-2*a-2):
            loops += 1
            c = 1000 - a - b
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print "Got it! {} {} {}".format(a, b, c)
                print "Product = {}".format(a*b*c)
                print "{} loops".format(loops)
                quit()


if __name__ == '__main__':
    main()
