def largest_bf(A):
    """
    largest subarray by brute force
    Number of subarrays scales with n^2
    >>> largest_bf([904,40,523,12,-335,-385,-124,481,-31])
    1479
    """
    return max([sum(A[i:j]) for i in range(len(A)) for j in range(len(A)) if i < j])

