#!/usr/bin/python3
""" A function that writes a string to a text file 
    (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """ Writes a string to a text file UTF-8
    Returns:
        The number of characters written.
    """
    with open(filename, "w") as myFile:
        myFile.seek(0, 2) # Move the file pointer to the end of the file
        numOfChars = myFile.write(text)
    return numOfChars
