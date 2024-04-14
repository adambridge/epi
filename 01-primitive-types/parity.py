def parity01(x):
    """
    O(n) where n it word size
    >>> parity01(0b0001)
    1
    >>> parity01(0b0010)
    1
    >>> parity01(0b0011)
    0
    >>> parity01(0b0101)
    0
    """
    result = 0
    while x > 0:
        result ^= x & 1 
        x >>= 1
    return result


def parity02(x):
    """
    Uses x = x & (x - 1) to zero lowest used bit.
    O(k) where k is number of non-zero bits.
    >>> parity02(0b0001)
    1
    >>> parity02(0b0010)
    1
    >>> parity02(0b0011)
    0
    >>> parity02(0b0101)
    0
    """
    result = 0
    while x > 0:
        x &= (x - 1) 
        result ^= 1
    return result


PRECOMPUTED_PARITY = {
    0b0000: 0,
    0b0001: 1,
    0b0010: 1,
    0b0011: 0,
    0b0100: 1,
    0b0101: 0,
    0b0110: 0,
    0b0111: 1,
    0b1000: 1,
    0b1001: 0,
    0b1010: 0,
    0b1011: 1,
    0b1100: 0,
    0b1101: 1,
    0b1110: 1,
    0b1111: 0,
}

def parity03(x):
    """
    Uses a lookup. Takes O(m) where m is word size / mask size but uses O(2^s) memory
    for the lookup where s is the word size.  
    >>> parity03(0b0101100000000000)
    1
    >>> parity03(0b1110000000100001)
    1
    >>> parity03(0b1011001101110011)
    0
    >>> parity03(0b1001011101010001)
    0
    """
    MASK_SIZE = 4
    MASK = 0b1111
    cache = PRECOMPUTED_PARITY
    return (cache[x & MASK] ^
            cache[x >> MASK_SIZE * 1 & MASK] ^
            cache[x >> MASK_SIZE * 2 & MASK] ^
            cache[x >> MASK_SIZE * 3 & MASK])


def parity04(x):
    """
    Uses the fact that parity of 01001110 = parity of 0100 xor 1110
    01001110 starting value
    00000100 shifted >> 4
    01001010 xor shifted with original (just ignore 1st 4 bits or result)
    00010010 shifted >> 2
    01011000 2nd xor (ignore 1st 6 bits)
    00101100 shifted >> 1
    01110100 3rd xor (last bit is partity of original bits)
    parity of last bit = 0
    Time complexity is O(log2(s)) for word size s
    >>> parity04(0b0101100000000000)
    1
    >>> parity04(0b1110000000100001)
    1
    >>> parity04(0b1011001101110011)
    0
    >>> parity04(0b1001011101010001)
    0
    """
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    x &= 1
    return x
           
    

