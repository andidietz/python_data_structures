def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    updated_phrase = ''
    
    for letter in phrase:
        if letter == to_swap.swapcase() or letter == to_swap: 
            updated_phrase += letter.swapcase()
        else:
            updated_phrase += letter
    return updated_phrase