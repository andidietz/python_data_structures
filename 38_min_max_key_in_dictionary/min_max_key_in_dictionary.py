def min_max_keys(dictionary):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    keys = list(dictionary.keys())

    # Source: Using min() and max() (6/24/2021): Exercise Solution
    # Source: Understanding min() (6/24/2021): https://www.geeksforgeeks.org/python-string-min/#:~:text=min()%20is%20an%20inbuilt,alphabetical%20character%20in%20a%20string.&text=Return%20value%3A,lowest%20character%20in%20the%20string.
    return (min(keys), max(keys))
 