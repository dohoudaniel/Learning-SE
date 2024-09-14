#!/usr/bin/python3
raise_exception_msg = __import__('task6').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

