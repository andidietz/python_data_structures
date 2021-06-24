def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    repeated_phrase = []

    if isinstance(num, int):
        i = 1
        while i < num + 1:
            repeated_phrase.append(phrase) 
            i += 1
    return ''.join(repeated_phrase)
