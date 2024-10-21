"""
Creates a random matrix with a specified size in rows.
"""

from random import randint

with open('input.csv', 'w', encoding='utf-8') as f:
    rows = 15
    matrix = []
    for _ in range(rows):
        matrix.append(', '.join([str(randint(0, 1)) for _ in range(rows)]) + '\n')
    f.writelines(matrix)
