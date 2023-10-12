#!/usr/bin/python3
""" Function for the implementation of minimum operations"""


def minOperations(n):
    """
    Method wchich calculates the fewest number of operations needed.
    """
    # check output size to be at least 2 characters.
    if (n < 2):
        return 0
    base_operation = 0
    root_operation = 2
    while root_operation <= n:
        if n % root == 0:
            base_operation += root_operation
            n = n / root_operation
            root_operation -= 1
        
        root_operation += 1
    return base_operation
