#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    result = [[1]]
    for _ in range(1, n):
        row = [1]
        for j in range(1, len(result[-1])):
            row.append(result[-1][j - 1] + result[-1][j])
        row.append(1)
        result.append(row)

    return result
