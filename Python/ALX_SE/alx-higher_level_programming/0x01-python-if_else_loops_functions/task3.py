#!/usr/bin/python3
for i in range(97, 123):
    if i != 113 and i != 101:	# In the ASCII Table, 101 is 'e' and 113 is 'q'
        print('{:c}'.format(i), end='')

