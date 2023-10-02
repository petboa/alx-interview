#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] if i == 0 else [1, 1]

        if i >= 2:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                value = prev_row[j - 1] + prev_row[j]
                row.insert(j, value)

        triangle.append(row)

    return triangle
