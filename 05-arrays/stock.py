
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
