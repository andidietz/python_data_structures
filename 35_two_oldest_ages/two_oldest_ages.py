def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    # """
    # # Source: reverse arg for sorted() (6/24/2021): https://www.w3schools.com/python/ref_func_sorted.asp
    sorted_ages = sorted(ages, reverse=True)
    oldest = sorted_ages[0]

    for age in sorted_ages:
        if age != oldest:
            return (age, oldest)

