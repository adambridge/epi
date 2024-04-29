def partition(array, pivot):
    """
    Partition array around element at index pivot
    First get value of pivot
    Start at either end (i/j) and compare to pivot
    while i != j
    If Ai < Ap increment i
    If Aj > Ap decrement j
    If Ai == Ap look onwards for < Ap, swap with Ai, and increment i to index where found (i + offset)
               i     i+2
    p = 1, [0, 1, 1, 0, ...]
    Likewise for j end...

    If i > p and j < p swap them then increment i and decrement j

    >>> A = [2, 1, 0, 2, 1, 0]
    >>> partition(A, 1)
    >>> A
    [0, 0, 1, 1, 2, 2]
    """
    i, j, offset = 0, len(array) - 1, 0
    while True:
        while i < pivot and array[i] <= array[pivot]:
            while array[i + offset] == array[pivot]:
                offset += 1
            if offset > 0:
                array[i], array[i + offset] = array[i + offset], array[i]
                i, offset = i + offset, 0
            i += 1
        while j > pivot and array[j] >= array[pivot]:
            while array[j - offset] == array[pivot]:
                offset += 1
            if offset > 0:
                array[j], array[j - offset] = array[j + offset], array[j]
                j, offset = j - offset, 0
            j -= 1
        if i == j:
            break
        else:
            array[i], array[j] = array[j], array[i]


