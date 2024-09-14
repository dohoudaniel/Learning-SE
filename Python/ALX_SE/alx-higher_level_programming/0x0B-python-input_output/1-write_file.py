#!/usr/bin/python3
""" A function that writes a string to a text file 
    (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file UTF-8
    Returns:
        The number of characters written.
    """
    with open(filename, "w") as myFile:
        numOfChars = myFile.write(text)
    return numOfChars
