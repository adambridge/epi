def fib(n):
    """
    uncached, O(exp) since calling fib(n) calls fib n-1 times and each those calls makes _ calls, etc
    >>> fib(10)
    55
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def cfib(n, cache={}):
    """
    cached for O(n) time at cost of O(n) space
    fun fact: in python default arguments are evaluated on function definition.
    As a result the cache doesn't need to be passed to subsequent invocations
    >>> cfib(10)
    55
    """
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = cfib(n - 1) + cfib(n - 2)

    return cache[n]


def ifib(n):
    """
    Iteratively method for O(1) space complexity
    Notes: for _ in ... preferable if variable is not used, range(1, n) is a neat alternative to range(n - 1) here
    >>> ifib(10)
    55
    """
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1

    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
        
    return f



