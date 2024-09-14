"""
An algorithm that finds the square root of a number
"""

# Import statements
from time import sleep


def square_root(y):
    """
    A function that checks for the square root of a number

    x: Integer
    y: Integer
    """
    if y > 0:
        y = int(y)
        message = "Finding square root of "
        my_length = len(message)
        for i in range(my_length):
            # print(message[i], end="")
            # sleep(0.05)
            pass
        # sleep(0.05)
        # print("{:d}".format(y))
        # sleep(2)
    else:
        message = "Error: Cannot find square root of a negative number."
        my_length = len(message)
        for i in range(my_length):
            # print(message[i], end="")
            # sleep(0.05)
            pass
        # sleep(0.05)
    z = y + 1
    for x in range(1, z):
        if y / x == x:
            # print("{:d} is the square root of {:d}".format(x, y))
            # print()
            break
        elif x == y:
            # print("{:d} has no whole number square root".format(y))
            pass
        else:
            continue
    return x


if __name__ == "__main__":
    y = input("Enter a value for y: ")
    try:
        y = int(y)
        print()
        square_root(y)
    except Exception:
        message = "Input was not an integer.\nTry again with an int :)."
        temp = len(message)
        for i in range(temp):
            print(message[i], end="")
            sleep(0.05)
        sleep(0.05)

