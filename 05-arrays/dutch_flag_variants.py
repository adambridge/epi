
def partition_v1(A):
    """
    Group the values in any order, use the order they occur, so A[0] is always in group 0
    group 0: A[:p0]
    group 1: A[p0:p1]
    group 2: A[p1:p2]
    unclassified: A[p2:]

    >>> A = [2,2,1,0,2,1,2,2,1,0]
    >>> partition_v1(A)
    >>> A
    [2, 2, 2, 2, 2, 1, 1, 1, 0, 0]
    """
    p0, p1, p2 = 1, 1, 1
    while p2 < len(A):
        if A[p2] == A[0]:
            A[p2], A[p0] = A[p0], A[p2]
            p0, p1, p2 = p0 + 1, p1 + 1, p2 + 1
        elif p0 == p1 or A[p2] == A[p1 - 1]:
            A[p2], A[p1] = A[p1], A[p2]
            p1, p2 = p1 + 1, p2 + 1
        else:
            p2 = p2 + 1

