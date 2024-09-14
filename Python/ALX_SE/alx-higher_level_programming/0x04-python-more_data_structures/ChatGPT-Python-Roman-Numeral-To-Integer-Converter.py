#CHATGPT's Python Roman-Numeral-To-Integer Converter
# Prompt used: Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
#Response:
"""
Here's a Python function that takes a Roman numeral
string as input and returns the corresponding integer value:
"""
#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_val = 0
    for char in roman_string:
        val = roman_dict[char]
        if val > prev_val:
            total += val - 2 * prev_val
        else:
            total += val
        prev_val = val
    return total
"""
The function uses a dictionary to map each Roman numeral to its corresponding
integer value. It then loops through each character in the input string and
calculates the corresponding integer value. If the current value is greater
than the previous value, it subtracts twice the previous value from the
current value (this is to account for the fact that the previous value
was already added in the previous iteration). Otherwise, it simply
adds the current value to the total. Finally, the total value is returned.
"""

