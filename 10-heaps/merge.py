import heapq as hq
from collections import namedtuple

def my_merge(sequences):
    """
    Merge a set (s) of sorted sequences and compute their union as a sorted sequence
    Brute force would concatenate and sort at O(n log n) but doesn't take advantage of
    fact that lists are already sorted.
    How about sequentially taking the min of the first elements of each of the sequences?
    Is that where the min-heap comes in? How is that better? Surely heapifying these elements
    is no faster than just finding the min each time? -> The trick is heapification only
    needs to happen once, thereafter removing min and adding new elements are both O(log n)
    
    Brainfart: heapq.heapify(list) is in-place, returns None

    Note: list(heapq.merge(*sorted_arrays)) is how you would actually do this
    """
    ValAndId = namedtuple('ValAndId', ('value', 'id')) # sort order on first attribute: value

    iter_dict = {iter_id: iter(seq) for iter_id, seq in enumerate(sequences)}
    min_heap = [ValAndId(next(it), iter_id) for iter_id, it in iter_dict.items()]
    hq.heapify(min_heap)
    
    merged = []

    while min_heap:
        next_value, iter_id = hq.heappop(min_heap)
        merged.append(next_value)
        try:
            next_smallest = ValAndId(next(iter_dict[iter_id]), iter_id)
            hq.heappush(min_heap, next_smallest)
        except StopIteration:
            pass

    return merged


# my_merge([[0,1,2,3],[4,5,6,7]])
