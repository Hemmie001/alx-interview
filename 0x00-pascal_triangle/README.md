alx-interview


#!/usr/bin/python
"""
0-pascal_triangle
"""

def pascal_triangle(n): # defines a function named pascal_triangle
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0: # checks that n is a +ve no else returns an empty list
        return []

    result = [[1]] # initializes the result variable as a list containing a list with a single element, which is 1.This represents the first row of Pascal's triangle.
    for _ in range(1, n): # starts a loop that iterates from 1 to n-1(exclusive).The underscore is often used as a throwaway variable when the variable itself is not used inside the loop.
        row = [1] # Inside the loop, a new list row is created with the first element set to 1
        for j in range(1, len(result[-1])): # starts another nested loop, which iterats over the indices of the last row in the result list (excluding the first element).
            row.append(result[-1][j - 1] + result[-1][j]) # calculats the row's element by summing the corresponding elements from the last row of the result list.
        row.append(1) # After the nested loop, the last element (1) is appended to the row list. 
        result.append(row) # append to the result list, the row list representing a new row in Pascal's triangle, is appended to the result list.

    return result #  returns the generated Pascal's triangle stored in the result list
