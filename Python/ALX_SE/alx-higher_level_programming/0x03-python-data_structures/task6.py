#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ A Function that prints a matrix of integers """
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if b != 0 and b > 0:
                print(" ", end='')       # Prints the spaces between the integers.
            print("{:d}".format(matrix[a][b]), end='')
        print()    # This prints a newline.

