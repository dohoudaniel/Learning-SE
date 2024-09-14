# Define a 'repeat' function that takes two arguments
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times
    If exclaim is true, add exclamation marks
    """
    
    result = s + s + s   # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

# Updating this file
def main():
    print(repeat('Yay', False))      ## YayYayYay
    print(repeat('Woo Hoo', True))   ## Woo HooWoo HooWoo Hoo!!!

import sys
# Now we can refer to the sys.xxx facilities
sys.exit(0)
