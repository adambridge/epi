
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
            # 1st unclasified goes to 1st g1, 1st g1 goes to 1st uc but then reabsorbed into
            # g1 when p1 is increased
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
            


def partition_v2(A):
    """
    Group 4 values in any order

    group 0: A[:p0]
    group 1: A[p0:p1]
    group 2: A[p1:p2]
    unclassified: A[p2:p3]   so A[p2] is incoming element
    group 3: A[p3:]

    >>> A = [2, 1, 0, 3, 1, 0]
    >>> partition_v2(A)
    >>> A
    [2, 1, 1, 0, 0, 3]

    >>> A = [2,0,3,1,0,0,0,1,1,2,2,1,3,2,1,2,3,1,0]
    >>> partition_v2(A)
    >>> A
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1]
    """
    p0, p1, p2, p3 = 0, 0, 0, len(A)
    while p3 > p2:
        if A[p2] == A[0]:
            # same idea as partition_v1 but now need an extra shuffle
            # to shift everything up a group
            A[p0], A[p1], A[p2] = A[p2], A[p0], A[p1]
            p0, p1, p2 = p0 + 1, p1 + 1, p2 + 1
        elif p0 == p1 or A[p2] == A[p0]:
            A[p2], A[p1] = A[p1], A[p2]
            p1, p2 = p1 + 1, p2 + 1
        elif p1 == p2 or A[p2] == A[p1]:
            p2 += 1
        elif p3 == len(A) or A[p2] == A[p3]:
            A[p2], A[p3 - 1] = A[p3 - 1], A[p2]
            p3 -= 1


