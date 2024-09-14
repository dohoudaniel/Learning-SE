#!/usr/bin/python3
c = compile('def hello():\n\tprint("Hello World!")\nhello()', '', "exec")
exec(c)
# hello.__code__.co_code
# c.co_code
