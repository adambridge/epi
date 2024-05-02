from math import log

def str2int(s):
    """
    convert string to integer (the hard way!)
    don't bother about -ve
    >>> str2int('123')
    123
    """
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    for i, c in enumerate(s):
        result += d[c] * 10 ** (len(s) - i - 1)
    return result


def int2str(n):
    """
    >>> int2str(123):
    123

    """
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    digits_remaining = int(log(n, 10)) + 1 
    result = ""
    while digits_remaining > 0:
        factor = 10 ** (digits_remaining - 1)
        digit = n // factor
        result += d[digit] 
        n -= digit * factor
        digits_remaining -= 1
    return result
