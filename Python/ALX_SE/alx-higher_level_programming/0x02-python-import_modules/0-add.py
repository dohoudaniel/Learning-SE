#!/usr/bin/python3

if __name__ == "__main__":

    from add_0 import add
    
    a = 1
    b = 2

    a = int(a)
    b = int(b)

    print("{} + {} = {}".format(a, b, add(a, b)))
