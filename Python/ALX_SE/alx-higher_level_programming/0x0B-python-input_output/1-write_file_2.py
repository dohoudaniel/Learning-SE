#!/usr/bin/python3
""" A function that that writes a string to a text file (UTF8)
    and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF-8)
    Returns:
        Nothing.
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        num_chars = 0
        for char in text:
            myFile.write(char)
            num_chars += 1
        return num_chars

