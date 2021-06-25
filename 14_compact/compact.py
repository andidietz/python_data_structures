def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # Source: Accessing index in python for loop (6/21/2021): https://realpython.com/python-enumerate/
    # Source: Understanding Enumrate args (6/21/2021): https://www.geeksforgeeks.org/enumerate-in-python/
    for count, item in enumerate(lst, start=0):
        if not item:
            lst.pop(count)
    return lst
