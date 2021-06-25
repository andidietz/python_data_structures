def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    frequency = {}
    
    for num in nums:
        if num not in frequency:
            frequency[num] = nums.count(num)

    vals = list(frequency.values())
    vals.sort(reverse = True)
    
    # Source: Get key from value (6/21/2021):https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    for num, count in frequency.items():
        if count == vals[0]:
            return num
