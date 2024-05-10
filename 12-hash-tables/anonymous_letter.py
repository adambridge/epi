from collections import Counter

def is_constructible(letter, magazine):
    letter_counter, magazine_counter = Counter(letter), Counter(magazine)
    """
    Return True if ransom note `letter` can be contructed from letters in `magazine` else False
    (My attempt)
    >>> is_constructible("money by noon", "cats are good")
    False
    >>> is_constructible("money by noon", "no one needs to buy yams")
    True
    """
    return all(lv <= magazine_counter[lk] for lk, lv in letter_counter.items()) 

def book_contstructible(letter, magazine):
    """
    Neat pythonic book solution
    >>> is_constructible("money by noon", "cats are good")
    False
    >>> is_constructible("money by noon", "no one needs to buy yams")
    True
    """
    return not Counter(magazine) - Counter(letter)
