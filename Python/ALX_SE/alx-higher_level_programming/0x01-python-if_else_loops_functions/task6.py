#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x == 8 and y == 9:
            print('{}{}'.format(x, y))
        elif x != y and x < y:
            print('{}{}, '.format(x, y), end='')

