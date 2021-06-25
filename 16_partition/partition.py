def partition(lst, func):
    """Partition lst by predicate.
     
     - lst: list of items
     - func: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed func test,
     and `b` are items that failed func test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    passed_test = []
    failed_test = []

    for item in lst:
        result = func(item)
        if result:
            passed_test.append(item)
        else:
            failed_test.append(item)
    return [passed_test, failed_test]

def is_even(num):
        return num % 2 == 0
        
def is_string(el):
        return isinstance(el, str)