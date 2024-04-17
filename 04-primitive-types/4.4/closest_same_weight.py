COUNT = {
    0b0000: 0,
    0b0001: 1,
    0b0010: 1,
    0b0011: 2,
    0b0100: 1,
    0b0101: 2,
    0b0110: 2,
    0b0111: 3,
    0b1000: 1,
    0b1001: 2,
    0b1010: 2,
    0b1011: 3,
    0b1100: 2,
    0b1101: 3,
    0b1110: 3,
    0b1111: 4,
}

def bit_count(x):
    mask_size = 4
    mask = 0b1111
    return (COUNT[x & mask] + COUNT[x >> mask_size & mask]
          + COUNT[x >> mask_size * 2 & mask]
          + COUNT[x >> mask_size * 3 & mask])


def my_closest(x):
    """
    Return an integer as close as possible to the input (but not equal)
    with the same number of bits set.
    My attempt before looking at the solution, counting could be done
    by counting setting LSB to zero x &= (x - 1) or by cache (as here).
    Once count is known, identify nearest with same weight.
    >>> f"{my_closest(0b110):b}"
    '101'
    """
    count = bit_count(x)
    i, j = 1, 1
    while (True):
        if bit_count(x - i) == count and x - i > 0:
            return x - i 
        elif bit_count(x + j) == count and x + j < 0xffff:
            return x + j
        if x - i > 0:
            i += 1
        if x + j < 0xffff:
            j += 1 



def closest(x):
    """
    Naive solution of checking each value (as in my_closest()) is slow for some values.
    Best solution is to swap rightmost differing adjacent bits.
    My attempt at implementing after reading book solution.
    >>> f"{my_closest(0b110):b}"
    '101'
    """
    word_size = 64
    count = bit_count(x)
    for i in range(word_size):
        if x >> i & 1 == x >> i + 1 & 1:
            mask = 1 << i | 1 << i + 1
            x ^= mask
            break
    return x
