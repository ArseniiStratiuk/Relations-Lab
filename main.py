"""
Discrete mathematics relations laboratory project.
"""
from copy import deepcopy
from time import monotonic
from itertools import product


def read_file(filename: str) -> list[list[int]]:
    """
    Read matrix from a file and transform it into a list of lists.

    :param filename: str, A path to the file.
    :return: list[list[int]], A matrix that was read from a file.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w", delete=False) as tmp:
    ...     _ = tmp.write('0, 0, 1\\n0, 1, 1\\n1, 1, 1\\n')
    >>> read_file(tmp.name)
    [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    matrix = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            row = []
            for i in line.strip().split(','):
                row.append(int(i.strip()))
            matrix.append(row)

    return matrix


def write_file(filename: str, relation: list[list[int]]) -> None:
    """
    Create a file with input from the matrix.

    :param filename: str, A path to the file.
    :param relation: list[list[int]], A matrix to write into the file.
    :return: None

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w", delete=False) as tmp:
    ...     _ = tmp.write('')
    >>> write_file(tmp.name, [[0, 1, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1]])
    >>> with open(tmp.name, "r", encoding="utf-8") as file:
    ...     print(file.read())
    0, 1, 0, 0
    1, 1, 1, 1
    1, 0, 0, 0
    1, 1, 1, 1
    <BLANKLINE>
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for row in relation:
            line = []
            for i in row:
                line.append(str(i))
            f.write(', '.join(line) + '\n')


def symmetric_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Find the symmetric closure of the matrix.

    :param matrix: list[list[int]], An input relation represented as a matrix.
    :return: list[list[int]], The symmetric closure of the input relation
    represented as a matrix.

    >>> matrix = [[0, 1, 1], [0, 0, 1], [0, 1, 1]]
    >>> print(symmetric_closure(matrix))
    [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
    """
    new_pairs = []
    symmetric_matrix = deepcopy(matrix)
    for row, line in enumerate(matrix):
        for column, value in enumerate(line):
            if value:
                # Note a symmetric pair that has to be included.
                new_pairs.append((column, row))

    for pair in new_pairs:
        row, column = pair
        symmetric_matrix[row][column] = 1

    return symmetric_matrix


def reflexive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Find the reflexive closure of the matrix.

    :param matrix: list[list[int]], An input relation represented as a matrix.
    :return: list[list[int]], The reflexive closure of the input relation
    represented as a matrix.

    >>> matrix = [[0, 1, 1], [0, 0, 1], [0, 1, 1]]
    >>> print(reflexive_closure(matrix))
    [[1, 1, 1], [0, 1, 1], [0, 1, 1]]
    """
    reflexive_matrix = deepcopy(matrix)
    for column, row in enumerate(reflexive_matrix):
        row[column] = 1

    return reflexive_matrix


def transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Find the transitive closure of the matrix using the Warshall algorithm.

    :param matrix: list[list[int]], An input relation represented as a matrix.
    :return: list[list[int]], The transitive closure of the input relation
    represented as a matrix.

    >>> matrix = [[0, 1, 1], [0, 0, 1], [0, 1, 1]]
    >>> print(transitive_closure(matrix))
    [[0, 1, 1], [0, 1, 1], [0, 1, 1]]
    """
    length = len(matrix)
    transitive_matrix = deepcopy(matrix)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                # If there is a path from i to k and from k to j,
                # then there is a path from i to j.
                transitive_matrix[i][j] = (
                    transitive_matrix[i][j] | (transitive_matrix[i][k] & transitive_matrix[k][j])
                )

    return transitive_matrix


def split_into_classes(matrix: list[list[int]]) -> list[list[int]]:
    """
    Split the relation into equivalence classes.

    >>> split_into_classes([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
    [[0, 1, 2], [3]]
    >>> split_into_classes([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    [[0], [1], [2], [3]]
    >>> split_into_classes([[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
    [[0, 3], [1], [2]]
    >>> split_into_classes([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
    [[0, 3], [1, 2]]
    >>> split_into_classes([[1, 0, 1, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1]])
    [[]]
    """
    if transitive_closure(
            symmetric_closure(
                reflexive_closure(matrix)
            )
    ) != matrix:
        return [[]]

    n = len(matrix)
    classes = list()
    included = set()
    for i in range(n):
        if i not in included:
            class_ = [j for j in range(n) if matrix[i][j]]
            included = included.union(class_)
            classes.append(class_)

    return classes


def is_transitive(matrix: list[list[int]]) -> bool:
    """
    Check if the given relation is transitive. Return True if yes, otherwise False.

    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    False
    """
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            row_i = matrix[i]
            if i != j and row_i[j]:
                row_j = matrix[j]
                for k in range(length):
                    if row_j[k] and not row_i[k]:
                        return False

    return True


def transitive_number(number: int) -> int:
    """
    Return how many transitive relations are there on relation with n elements.

    :param number: int, Must be <= 6.

    >>> transitive_number(0)
    1
    >>> transitive_number(2)
    13
    >>> transitive_number(3)
    171
    >>> transitive_number(4)
    3994
    >>> transitive_number(5)
    154303
    """
    count = 0
    start = monotonic()
    # get all binary variations from 1 to 2^total_elements using a product generator
    for binary_tuple in product((0, 1), repeat=number * number):
        # form a matrix [[i1j1...i1jn],...[inj1...injn]]
        matrix = [
            list(binary_tuple[i * number:(i + 1) * number])
            for i in range(number)
        ]
        count += is_transitive(matrix)

    print(f"Time: {monotonic() - start} s")

    return count


if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())

    input_matrix = read_file('input.csv')
    result = transitive_closure(input_matrix)
    write_file('output.csv', result)
