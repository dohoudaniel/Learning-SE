#!/usr/bin/python3
""" A function that reads a text file. """


def read_file(filename=""):
    """  Reads a text file (UTF-8) and prints it to stdout
    Returns:
        Nothing.
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
