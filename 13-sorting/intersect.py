def my_intersect(a, b):
    """
    Return the intersection of two sorted lists (no duplicates) my attempt
    Iterate both lists, if elem equal append to new, increment if either equal
    to last added, if not equal increment lower (brutish solution?)
    Time complexity O(len(a) * len(b))
    >>> my_intersect([0,1,2,3,4,5], [2,2,3])
    [2, 3]
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

