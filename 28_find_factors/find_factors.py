def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # Source: factoring (6/22/2021): https://www.programiz.com/python-programming/examples/factor-number
    return [num_in_range for num_in_range in range(1, num + 1) if num % num_in_range == 0]
