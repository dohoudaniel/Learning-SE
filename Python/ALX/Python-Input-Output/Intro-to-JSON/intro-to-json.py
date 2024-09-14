#!/usr/bin/python3

""" First Introduction to JSON """

# import os
import json

""" Viewing the JSON string representation of an object """
# An object 'x'
x = [1, 'simple', 'list']

# Using the dumps() method
Json1 = json.dumps(x)
print(Json1)

# Using the dump() method
# Another variant of the dumps() function, called dump(),
# simply serializes the object to a text file.
# If f is a text file object opened for writing, we can do this
# Json2 = json.dump(x, f)
# print(Json2)

# To decode the object again, if f is a binary file or text file
# object which has been opened for reading:


