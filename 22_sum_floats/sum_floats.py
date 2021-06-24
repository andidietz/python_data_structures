def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # Source: isinstance function (6/22/2021): https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
    floats = []
    
    for item in nums:
        if isinstance(item, float):
            floats.append(item)
    return sum(floats)    