"""
GCD of 25 and 15
= GCD of 25-15 and 15
= GCD of 10 and 15
= GCD of 15-10 and 10
= GCD of 5 and 10
= GCD of 10-5 and 5
= GCD of 5 and 5
= 5

In that case y % x would be no different to y - x but 

GCD of 28 and 7
= GCD of 21 and 7
= GCD of 14 and 7
= GCD of 7 and 7

is quicker with modulus

GCD of 28 and 7
= GCD of 28 % 7 and 7
= GCD of 0 and 7
"""

def gcd(x, y):
    """
    gcd(15, 25)
    gcd(10, 15)
    gcd(5, 10)
    gcd(5, 5)
    gcd(0, 5)
    >>> gcd(15, 25)
    5
    >>> gcd(7, 28)
    7
    """
    return y if x == 0 else gcd(y % x, x)


