def naive_reverse_bits(x):
    """
    Reverse the bits in a 64 bit integer.
    My attempt before looking at the book solution
    Hint says to use a lookup table but right now I don't understand why...
    I think I'll first do it without to gain some intuition.
    Also just doing 8 bits but should work for 64 just the same
    >>> f"{naive_reverse_bits(0b10010111):b}"
    '11101001'
    """
    i, result = x.bit_length() - 1, 0
    while i >= 0:
        if x & 1 << i != 0:
            result |= 1 << x.bit_length() - 1 - i
        i -= 1
    return result


def reverse_bits_in_place(x):
    """
    As above but swap bits in place, only have to iterate half way and use less memory
    01234567
    7 <> 0
    6 <> 1
    5 <> 2
    4 <> 3
    >>> f"{reverse_bits_in_place(0b10010111):b}"
    '11101001'
    """
    i = 0
    while i < x.bit_length() // 2:
        hi_bit = x >> x.bit_length() - 1 - i & 1
        lo_bit = x >> i & 1
        if hi_bit != lo_bit:
            mask = 1 << i | 1 << x.bit_length() - 1 - i
            x ^= mask
        i += 1
    return x


REVERSED = {
    0b0000: 0b0000,
    0b0001: 0b1000,
    0b0010: 0b0100,
    0b0011: 0b1100,
    0b0100: 0b0010,
    0b0101: 0b1010,
    0b0110: 0b0110,
    0b0111: 0b1110,
    0b1000: 0b0001,
    0b1001: 0b1001,
    0b1010: 0b0101,
    0b1011: 0b1101,
    0b1100: 0b0011,
    0b1101: 0b1011,
    0b1110: 0b0111,
    0b1111: 0b1111,
}

def cache_reverse_16_bits(x):
    """
    Precomputed cache solution, e.g. divide into 4x 16 bit integers so 2**16 keys in lookup.
    Illustrate here with 2**4 keys to reverse a 16 bit integer.
    Time complexity is O(n/L) for n chunks of length L
    >>> f"{cache_reverse_16_bits(0b0001010111111011):b}"
    '1101111110101000'
    """
    mask_size = 4
    mask = 0b1111
    return (REVERSED[x & mask] << mask_size * 3 | 
            REVERSED[x >> mask_size & mask] << mask_size * 2 |
            REVERSED[x >> mask_size * 2 & mask] << mask_size * 1 |
            REVERSED[x >> mask_size * 3 & mask])




