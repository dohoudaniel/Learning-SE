#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers in a matrix """
    if not matrix:
        return None
    
    number_list = []
    daniel = list(list(map(lambda a: a * a, number_list)) for number_list in matrix)
    return daniel

