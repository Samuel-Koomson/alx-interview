#!/usr/bin/python3

def pascal_triangle(n):
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
    triangle = []

    # checking if n is less than or equal to 0
    if n <= 0:
        return triangle

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
               row.append(1)
            else:
                # Calculate the middle elements using the values from the previous row
                prev_row = triangle[i - 1]
                middle_element = prev_row[j - 1] + prev_row[j]
                row.append(middle_element)

        triangle.append(row)

    return triangle

# Function test
if __name__ == "__main__":
    n = 5
    result = generate_pascals_triangle(n)
    for row in result:
        print(row)

