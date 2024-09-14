#!/usr/bin/python3

# The reverse() method reverses the sorting order of the elements.
for i in reversed(range(97, 123)):
    if (i % 2 == 0):
        print('{:c}'.format(i), end='')		# prints lowercase if i is an even number
    else:
        print('{:c}'.format(i - 32), end='')	# prints uppercase if i is an odd number

