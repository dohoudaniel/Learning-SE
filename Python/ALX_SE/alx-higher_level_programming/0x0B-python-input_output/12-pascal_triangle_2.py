#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to a given level n.

    Args:
        n (int): The level of Pascal's Triangle to generate.

    Returns:
        list: List of lists representing Pascal's Triangle.

    Raises:
        None

    """
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = []  # List to store the rows of Pascal's triangle

    # Initialize the first row
    triangle.append([1])

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]  # Start each row with 1

        # Calculate values for the current row
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)

        row.append(1)  # Append 1 at the end of each row
        triangle.append(row)

    return triangle
