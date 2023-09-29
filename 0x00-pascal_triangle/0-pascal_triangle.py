#!/usr/bin/python3

"""
Generate Pascal's triangle up to the nth row.
Args:
n (int): The number of rows to be generated.

Returns:
list: A list of lists which represents Pascal's triangle.
"""


def pascal_triangle(n):
    """Function for the making of pascal triangle"""
    triangle = []
    # check if the triangle is less than 0
    if n <= 0:
        return triangle
    for i in range(n):
        initial_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                initial_list.append(1)
            else:
                initial_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(initial_list)
    return triangle
