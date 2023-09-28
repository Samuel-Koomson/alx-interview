#!/usr/bin/python3
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows to be generated.

    Returns:
    list: A list of lists which represents Pascal's triangle.

    Example:
    pascals_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
def pascal_triangle(n):
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
