#!/usr/bin/python3

"""
Match statements
Simple implementation.
"""

name = str(input("lease enter your name: "))
match name:
    case "Daniel":
        print("Welcome home, Daniel.")
    case "Barry Allen":
        print("Welcome home, Flash.")
    case _:
        print("I don't know you, stranger.\nHelp!!!")

# The match statements can be implemented in much more complex ways.
