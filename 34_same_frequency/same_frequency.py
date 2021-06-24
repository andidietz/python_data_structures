def count_frequency(num):
    frequency = {}

    # Source: Turning Int into List (6/23/2021): https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
    individual_digits = [int(digit) for digit in str(num)]
    
    for digit in individual_digits: 
        frequency[digit] = str(num).count(str(digit))
    return frequency

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    frequency_1 = count_frequency(num1)
    frequency_2 = count_frequency(num2)
    
    return frequency_1 == frequency_2
