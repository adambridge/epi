
def my_first_k(A, k):
    """
    Return the index of the *first* occurrence of k in sorted array A
    or -1 if not found - my attempt prior to reading solution.
    Start by implementing a regular binary_search?

    Post solution notes - one while loop should be enough
    >>> my_first_k([1,2,2,2,2,3,4,5,6], 2)
    1
    >>> my_first_k([-10,-5,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6], 2)
    3
    >>> my_first_k([-10,-5,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6], 2)
    3
    """
    l, u = 0, len(A) - 1
    located = False
    while l < u:
        m = l + (u - l) // 2
        if A[m] == k:
            located = True
            break
        elif A[m] < k:
            l = m + 1
        else:
            u = m - 1

    if located:
        # use another binary search to find first k
        u = m # set upper bound to index where previous k was found
        while l < u:
            m = l + (u - l) // 2
            if A[m] == k:
                u = m - 1
            elif A[m] < k:
                l = m + 1
        return l

    return -1


def my_revised_first_k(A, k):
    """
    Revised after checking book solution.

    Notes: while loop needs to wait for lower to go above upper in this version
    >>> my_revised_first_k([1,2,2,2,2,3,4,5,6], 2)
    1
    >>> my_revised_first_k([-10,-5,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6], 2)
    3
    """
    l, u = 0, len(A) - 1
    result = -1
    while l <= u:
        m = l + (u - l) // 2
        if A[m] > k:
            u = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            result = m
            u = m - 1

    return result
