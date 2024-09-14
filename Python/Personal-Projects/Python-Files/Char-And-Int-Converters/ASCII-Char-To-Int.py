# This is the Python Int to ASCII Char Converter file
# Author: Dohou Daniel
# Function: It converts any entered number into an ASCII character based on the ASCII Table
# Compile this way: python3 ASCII-Char-Converter-To-Int.py

print("Thank you for using the Python Converter.")
# print()
   
# Accepting from Standard Input
entry = input("Enter a character of your choice: ")
    
# Typecasting to an int
process = str(entry)
    
# Converting to an ASCII Character
answer = ord(process)
    
# Printing the character
print("The ASCII Character for {0} is {1}".format(entry, answer))

