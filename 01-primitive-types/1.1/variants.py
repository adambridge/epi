"""
Using only bitwise operators, equality checks and boolean operators
"""

def right_propagate(x):
    """
    One stragegy:
    01010000
    Isolate rightmost bit
    00010000
    Subtract 1
    00001111
    or/xor with original
    01011111
    >>> print(f"{right_propagate(0b01010000):b}")
    1011111
    """
    rightmost_bit = x & ~(x - 1)
    return x | rightmost_bit - 1
    

def mod_pow_2(x, n):
    """
    Compute x mod 2 ** n
    x: 77, n: 6 => 77 mod 2 ** 6 => 77 mod 64 => 13
    Strategy: 
    1. 2 ** n => 1 << n
    2. modulus
    77 => 1001101
    64 => 1000000
    modulus is 77 xor 64
       => 0001101
    >>> mod_pow_2(77, 6)
    13
    """
    return x ^ 1 << n


def is_pow_2(x):
    """
    Test if a number is a power of 2
    Strategy: is a power of 2 if only 1 bit is set,
    set lowerest set bit to zero, is a power of 2 if result is zero.
    Set lowest bit to 0: x & (x - 1)
    >>> is_pow_2(43)
    False
    >>> is_pow_2(64)
    True
    """
    return x & (x - 1) == 0

