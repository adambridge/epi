from functools import reduce
from math import log
from string import digits

def my_str2int(s):
    """
    convert string to integer (the hard way!)
    don't bother about -ve
    >>> my_str2int('123')
    123
    """
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    for i, c in enumerate(s):
        result += d[c] * 10 ** (len(s) - i - 1)
    return result


def my_int2str(n):
    """
    >>> my_int2str(123)
    '123'

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


def int2str_book(n):
    """
    As per book, n % 10 yeilds smallest digit. This gets the digits in reverse order,
    prepending would be expensive so append and reverse

    Also use chr() instead of dict

    >>> int2str_book1(123)
    '123'
    """
    result = ""
    while n > 0:
        result += chr(48 + n % 10)
        n = n // 10
    return ''.join(reversed(result))


def str2int_book(s):
    """
    what the fudge is this???
    s[s[0] == '|':]
    slice operator turns False into 0 and True into 1
    """
    return reduce(lambda result, c: result * 10 + digits.index(c), s, 0)
