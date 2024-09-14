#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """ A function that computes the square value of all integers of a matrix using map """
    daniel = list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
    return daniel

