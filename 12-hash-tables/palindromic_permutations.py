from collections import Counter

def has_palindromic_permutations(s):
    """
    Test whether the letters in string s can be rearranged to form a palindrome, my attempt
    True as long as no more than one character has an odd number of occurrences

    Use collections.Counter
    >>> has_palindromic_permutations("enough enough")
    True
    >>> has_palindromic_permutations("want to go on")
    False
    """
    counts = Counter(s) # frequency of each character in string s
    result = True
    found_odd = False
    for freq in counts.values():
        if freq % 2 == 1:
            if found_odd:
                result = False
                break
            found_odd = True
    return result


def can_form_palindrome(s):
    """
    Neat one line solution is possible using generator expression (similar syntax to list
    comprehension) and adding up frequencies mod 2 (0 for all even).
    >>> has_palindromic_permutations("enough enough")
    True
    >>> has_palindromic_permutations("want to go on")
    False
    """
    return sum(freq % 2 for freq in Counter(s).values()] <= 1

