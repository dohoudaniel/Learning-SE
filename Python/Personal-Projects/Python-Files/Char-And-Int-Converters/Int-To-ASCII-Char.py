# This is the Python Int to ASCII Char Converter file
# Author: Dohou Daniel
# Function: It converts any entered number into an ASCII character based on the ASCII Table
# Compile this way: python3 Int-To-ASCII-Char.py

#!/usr/bin/python3
print("Thank you for using the Python Converter.")
# print()
   
# Accepting from Standard Input
entry = eval(input("Enter an integer that you wish to convert: "))
    
# Typecasting to an int
process = int(entry)
    
# Converting to an ASCII Character
answer = chr(process)
    
# Printing the character
print("The ASCII Character for {0} is {1}".format(entry, answer))

