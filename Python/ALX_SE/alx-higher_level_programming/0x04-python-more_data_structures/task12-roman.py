#!/usr/bin/python3
def roman_to_int(roman_string):
    """ Converts a Roman Numeral to an integer """
    # Defined this dictionary roman using the Unicode for Roman Numerals
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # roman is a dictionary
    
    # Ensuring that roman_string is a string...
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    
    """ Notice how dictionaries and lists are used here """
    
    #<-->
    daniel = len(roman_string)
    integer_val = roman[roman_string[daniel - 1]]
    
    for d in range(daniel - 1, 0, -1):
        new_value = roman[roman_string[d]]
        old_value = roman[roman_string[d - 1]]
        
        if old_value >= new_value:
            integer_val = integer_val + old_value
        else:
            integer_val = integer_val - old_value
        
    return integer_val
            
