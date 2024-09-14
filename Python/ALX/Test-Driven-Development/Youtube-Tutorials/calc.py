#!/usr/bin/python3

""" This file contains basic math functions """

def add(x, y):
    """ Addition Function """
    return (x + y)

def subtract(x, y):
    """ Subtraction Function """
    return (x - y)

def multiply(x, y):
    """ Multiplication function """
    return (x * y)

def divide(x, y):
    """ Division function """
    if y == 0:
        raise ValueError("A division by zero cannot be performed.")
    return (x // y)
