def my_swap_bits(x, i, j):
    """
    Swap bits of 64 integer x in positions i and j
    LSB at index 0, MSB at 63
    My attempt before reading chapter.
    Strategy:
    1. Test if bits at i and j are set by performing AND with int where only that bit is set.
    Int with only bit i set: 1 << i
    0b00000001 << 1 = 0b00000010 
    & x (x = 73 aka 0b01001001):
    0b00000010 &
    0b01001001
    0b00000000 == 0 so bit 1 was not set

    0b00000001 << 6 = 0b01000000 
    & x (x = 73 aka 0b01001001):
    0b01000000 &
    0b01001001
    0b01000000 != 0 so bit 6 was set
    2. Set bits at i and j with their new values:
    bit 1 was not set so bit 6 must be set to 0.
    Know that bit 6 was originally 1 so change it with xor 0b01000000:
    0b01001001 ^
    0b01000000 
    0b00001001 bit 6 updated (intermediate result)
    bit 6 was set so bit 1 must be set to 1.
    Bit 1 was originally 0 so xor intermediate result with 0b00000010:
    0b00001001 ^
    0b00000010
    0b00001011 (result)

    >>> f"{my_swap_bits(0b01001001, 1, 6):b}"
    '1011'
    """
    ith_bit_value, jth_bit_value = 1 << i, 1 << j
    ith_bit_set, jth_bit_set = x & ith_bit_value == 0, x & jth_bit_value == 0
    if ith_bit_set == jth_bit_set:
        # i and j bits are the same so do nothing
        return x
    else:
        # i and j bits are different so toggle both
        return x ^ ith_bit_value ^ jth_bit_value
    

