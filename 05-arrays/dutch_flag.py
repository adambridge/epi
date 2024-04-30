
def my_partition(array, pivot):
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
    >>> my_partition(A, 1)
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


    """
    Book solutions
    1) Use O(n) additional memory by adding each element to a new array, smaller/equal/larger, return concatenation
    2) Avoid using additional memory, for each element, look at following elements to find one smaller than pivot.
    When found, swap with original element. Move elems smaller than pivot to front in this way. Repeat for larger starting
    from end and working back until reach one less than pivot. Is O(n^2) as for each element look at subsequent elements.
    3) Improved solution using subarrays. Index `smaller` tracks the first element not belonging to the group of elems smaller
    than the pivot (0 initially). Look at each element, if smaller than pivot, move it into the front group by swapping it with the element
    at index `smaller` and incrementing smaller. Do likewise for `larger` group in another pass.
    4) Best method (hopefully equivalent to mine?) is similar but with a single pass at the expense of addded complexity.
    The invariant subarrays used in this method are:
    bottom group: A[:smaller]
    middle group: A[smaller:equal]
    unclassified: A[equal:larger] (initially the entire array)
    top group: A[larger:]
    
    Also note that all book solutions used for i in range len(A) and for i in reversed(range(A))
    """

def partition_1(A, pivot_index):
    """
    My attempt at book solution 1 to check understanding
    Brain fart #1: A = smaller + equal + larger will not overwrite the original array, just our reference to it. Instead need to copy it in.
    Brain fart #2: iterating through array want range(len(array)) since range(n) yields 0 to n - 1
    >>> A = [2, 1, 0, 2, 1, 0]
    >>> partition_1(A, 1)
    >>> A
    [0, 0, 1, 1, 2, 2]
    """
    pivot = A[pivot_index]
    smaller, equal, larger = [], [], []
    for elem in A:
        if elem < pivot:
            smaller.append(elem)
        elif elem > pivot:
            larger.append(elem)
        else:
            equal.append(elem)
    i = 0
    for group in [smaller, equal, larger]:
        for j in range(len(group)):
            A[i] = group[j]
            i += 1


def partition_2(A, pivot_index):
    """
    My attempt at book solution 2 to check understanding
    >>> A = [2, 1, 0, 2, 1, 0]
    >>> partition_2(A, 1)
    >>> A
    [0, 0, 1, 1, 2, 2]
    Brain fart #1: serious trouble getting inner loop for 2nd pass iteration from back right.
    The trick was that the range is reduced by decreasing the stop index, not increasing the start index.
    Brain fart #2: asymmetry between front and back inner loops was hard to grok:
        j in range(i + 1, len(A))   i: 0, j: 1 2 3 4 5
                                    i: 1, j: 2 3 4 5
                                    ...
        vs
        j in range(i)               i: 5, j: 4 3 2 1 0
             (reversed)             i: 4, j: 3 2 1 0
    """
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

