"""
Reverse the bits in a 64 bit integer.
My attempt before looking at the book solution
Hint says to use a lookup table but right now I don't understand why...
I think I'll first do it without to gain some intuition.
Also just doing 8 bits but should work for 64 just the same
>>> f"{naive_reverse_bits(0b10010111):b}"
'11101001'
"""
def naive_reverse_bits(x):
    i, result = x.bit_length() - 1, 0
    while i >= 0:
        if x & 1 << i != 0:
            result |= 1 << x.bit_length() - 1 - i
        i -= 1
    return result




