#!/usr/bin/python3

# JSON Documentation
# Link: https://docs.python.org/3/library/json.html#module-json

import json

""" Encoding basic Python object hierachies """
firstVar = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(firstVar)

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

# io - Python's Standard Library Module for Input/Output
# import io
# from io import StringIO
# io = StringIO
# json.dump(['streaming API'], io)
# io.getValue()
""" For some reasons, this lines of code did not work """

print()


""" Compact encoding """
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))


""" Pretty printing """
# import json
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))


""" Decoding JSON """
# import json
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
print(json.loads('"\\"foo\\bar"'))
from io import StringIO
io = StringIO('["streaming API"]')
print(json.load(io))

# I shall stop here.
