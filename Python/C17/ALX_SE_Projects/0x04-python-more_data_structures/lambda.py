# Learning about the lambda, filter, reduce and map
# Link: https://python-course.eu/advanced-python/lambda-filter-reduce-map.php

"""
The Lambda function
"""
def mySum(x, y):
    return x + y


print(mySum(7, 10))

# A lambda function


def power(x, y):
    """
    A function that returns the power of x to y

    Args:
        x (int): An integer
        y (int): An integer

    Returns:
        z: An integer of the value x raised to y
    """
    z = x ** y
    return z


if __name__ == "__main__":
    print(power(3, 3))


"""
The map() functions
"""


def square(iterable):
    """
    """
    return iterable ** 2

anotherSum = lambda x, y: x ** y
print(anotherSum(3, 4))
