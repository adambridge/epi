from bisect import bisect_left

def my_intersect(a, b):
    """
    Return the intersection of two sorted lists (no duplicates) my attempt
    Iterate both lists, if elem equal append to new, increment if either equal
    to last added, if not equal increment lower (brutish solution? nope)
    Correction: time complexity not O(len(a) * len(b)) but O(len(a) + len(b))
    Improvements:
    1. Increment both after append and use whoile condition instead of break clause
    2. Check A[i - 0] if match rather than last_added and increment in same place as when matched
    >>> my_intersect([0,1,2,2,3,3,4,5,6], [2,2,3,4,4,5])
    [2, 3, 4, 5]
    """
    i, j, result, last_added = 0, 0, [], None
    while True:
        if a[i] != b[j]:
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        else:
            result.append(a[i])
            last_added = a[i]

        while last_added and i < len(a) and a[i] == last_added:
            i += 1
        while last_added and j < len(b) and b[j] == last_added:
            j += 1

        if i == len(a) or j == len(b):
            break

    return result


def book_brute_intersect(A, B):
    """
    So smol but inefficient O(len(a) * len(b)) time since searches whole of B for each in A
    enumerate used to look at last elem and remove duplicates
    >>> book_brute_intersect([0,1,2,2,3,3,4,5,6], [2,2,3,4,4,5])
    [2, 3, 4, 5]
    """
    return [a for i, a in enumerate(A) if a in B and (i == 0 or A[i] != A[i - 1])]


def book_bintree_intersect(A, B):
    """
    Use binary search for O(m log n) time, searching for elems from smaller array in larger
    >>> book_bintree_intersect([0,1,2,2,3,3,4,5,6], [2,2,3,4,4,5])
    [2, 3, 4, 5]
    """
    def found(e, E):
        return bisect_left(E, e)

    small, big = A, B if len(A) < len(B) else B, A 
    return [
        e for i, e in enumerate(small)
        if found(e, big) and (i == 0 or small[i] != small[i - 1])
    ]


def book_best_intersect(A, B):
    """
    Same method as mine neater implementation
    Reimplementing from memory to confirm successful grokkage
    >>> book_best_intersect([0,1,2,2,3,3,4,5,6], [2,2,3,4,4,5])
    [2, 3, 4, 5]
    """
    i, j, result 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == A[j]:
            if A[i] != A[i - 1]:
                result.append(A[i])
            i, j = i += 1, j += 1
        else if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result


