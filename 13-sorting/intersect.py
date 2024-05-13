def my_intersect(a, b):
    """
    Return the intersection of two sorted lists (no duplicates) my attempt
    Iterate both lists, if elem equal append to new, increment if either equal
    to last added, if not equal increment lower (brutish solution? nope)
    Correction: time complexity not O(len(a) * len(b)) but O(len(a) + len(b))
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


def book_intersect(A, B):
    """
    So smol but inefficient O(len(a) * len(b)) time since searches whole of B for each in A
    enumerate used to look at last elem and remove duplicates
    >>> my_intersect([0,1,2,2,3,3,4,5,6], [2,2,3,4,4,5])
    [2, 3, 4, 5]
    """
    return [a for i, a in enumerate(A) if a in B and (i == 0 or A[i] != A[i - 1])]
