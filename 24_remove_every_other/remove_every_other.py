def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # Source: Accessing every other item in list (6/22/2021): https://stackoverflow.com/questions/8865878/skipping-every-other-element-after-the-first
    return [lst[::2]]