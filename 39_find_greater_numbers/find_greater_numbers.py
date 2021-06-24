def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    total = 0
    lst_length = len(nums)
    
    # Source: Capturing the right nums parameters the Loops (6/24/2021): Exercise Solution
    for num1 in range(lst_length):
        for num2 in range(num1 + 1, lst_length):
            if nums[num2] > nums[num1]:
                total += 1
    return total