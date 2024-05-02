
def partition_v1(A):
    """
    Group 3 values in any order
    Are the values known in advance? Assume not since would be almost the same as book example
    Use group 0 for whatever is in A[0], assign other groups to whatever comes after

    group 0: A[:p0]
    group 1: A[p0:p1]
    unclassified: A[p1:p2]   so A[p1] is incoming element
    group 2: A[p2:]

    >>> A = [2, 1, 0, 2, 1, 0]
    >>> partition_v1(A)
    >>> A
    [2, 2, 1, 1, 0, 0]

    >>> A = [2,0,1,0,0,0,1,2,1,2,2,1,0,2,1,2,2,1,0]
    >>> partition_v1(A)
    >>> A
    [2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    """
    p0, p1, p2 = 0, 0, len(A)
    while p2 > p1:
        if A[p1] == A[0]:
            # group 0, swap with first of group 1 and increment p0 and p1
            A[p1], A[p0] = A[p0], A[p1]
            p0, p1 = p0 + 1, p1 + 1
        elif p0 == p1 or A[p1] == A[p0]:
            # i.e. group 1 is empty or incoming matches it
            # increment p1 to absorb it into group 1 from unclassified
            p1 += 1
        elif p2 == len(A) or A[p1] == A[p2]:
            # i.e. group 2 is empty or incoming matches it
            # swap with last of unclassified and decrement p2
            A[p1], A[p2 - 1] = A[p2 - 1], A[p1]
            p2 -= 1
            



