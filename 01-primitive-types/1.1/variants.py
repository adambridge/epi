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
    01011111
    """
    rightmost_bit = x & ~(x - 1)
    return x | rightmost_bit - 1
    

