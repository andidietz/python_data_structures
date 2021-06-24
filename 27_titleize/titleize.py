def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # Source: Titlecase method (6/22/21): https://www.geeksforgeeks.org/title-in-python/
    return phrase.title()