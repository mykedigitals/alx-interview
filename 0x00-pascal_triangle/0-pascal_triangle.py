#!/usr/bin/python3
"""determining pascal's triangle"""


def pascal_triangle(k):
    """
    returns list of Pascal’s triangle of m
    """
    triangle = []

    # return (trianlgle if k <= 0)
    if k <= 0:
        return triangle
    for v in range(k):
        temp_list = []

        for r in range(v+1):
            if r == 0 or r == v:
                temp_list.append(1)
            else:
                temp_list.append(triangle[v-1][r-1] + triangle[v-1][r])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
