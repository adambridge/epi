
def my_profit(A):
    """
    Max profit given a list of stock prices, first attempt.
    Keep track of profit and last min, if current - last min > profit, update it

    Mem O(1), Time O(n) for array of length n
    >>> my_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
    30
    """
    last_min, max_profit = A[0], 0
    for i in range(len(A)):
        if A[i] < last_min:
            last_min = A[i]
        profit = A[i] - last_min
        if profit > max_profit:
            max_profit = profit
    return max_profit


def longest_sub(A):
    """
    finds the length of the longest subarray of consecutive ints
    >>> longest_sub([1,0,0,0,2,3,3,3,3,4])
    4
    """
    prev, length, max_length = A[0], 1, 0
    for i in range(1, len(A)):
        if A[i] == prev:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
        prev = A[i]
    return max_length
    
