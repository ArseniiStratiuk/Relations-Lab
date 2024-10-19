"""
Discrete mathematics relations laboratory project.
"""
from copy import deepcopy


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


def cartesian_product(set_1: list[int],
                      set_2: list[int]) -> list[tuple[int, int]]:
    """
    Find the Cartesian product of two input sets.

    :param set_1: list[int], The first set represented as a list of integers.
    :param set_2: list[int], The second set represented as a list of integers.
    :return: list[tuple[int, int]], A list of the result pairs.

    >>> print(cartesian_product([1, 2], [0, 3]))
    [(1, 0), (1, 3), (2, 0), (2, 3)]
    >>> print(cartesian_product([1, 2], []))
    []
    """
    if len(set_1) == 0 or len(set_2) == 0:
        return []

    pairs = [(i, j) for i in set_1 for j in set_2]

    return pairs


def transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Find the transitive closure of the matrix.

    :param matrix: list[list[int]], An input relation represented as a matrix.
    :return: list[list[int]], The transitive closure of the input relation
    represented as a matrix.

    >>> matrix = [[0, 1, 1], [0, 0, 1], [0, 1, 1]]
    >>> print(transitive_closure(matrix))
    [[0, 1, 1], [0, 1, 1], [0, 1, 1]]
    """
    transitive_matrix = deepcopy(matrix)
    for column, row in enumerate(transitive_matrix):
        row = [idx for idx, val in enumerate(row) if val == 1]
        column = [idx for idx, row in enumerate(transitive_matrix) if row[column] == 1]
        new_pairs = cartesian_product(column, row)

        if len(new_pairs) == 0:
            continue

        for pair in new_pairs:
            row, column = pair
            transitive_matrix[row][column] = 1

    return transitive_matrix


def split_into_classes(matrix: list[list[int]]) -> list[list[int]]:
    """
    Split the relation into equivalence classes.

    >>> split_into_classes([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
    [[0, 1, 2], [3]]
    """
    pass


def is_transitive(matrix: list[list]) -> bool:
    """
    Check if the given relation is transitive. Return True if yes, otherwise False.

    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    False
    """
    pass


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
    """
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    # input_matrix = read_file('input.csv')
    # result = transitive_closure(input_matrix)
    # write_file('output.csv', result)
