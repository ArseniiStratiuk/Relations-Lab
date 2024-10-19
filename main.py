"""
Discrete mathematics relations laboratory project.
"""


def read_file(filename: str) -> list[list[int]]:
    """
    Read matrix from a file and transform it into a list of lists.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w", delete=False) as tmp:
    ...     _ = tmp.write('001\\n011\\n111')
    >>> read_file(tmp.name)
    [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    pass


def write_to_file(filename: str, relation: list[list[int]]) -> None:
    """
    Create a file with input from {matrix}.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w", delete=False) as tmp:
    ...     _ = tmp.write('')
    >>> write_to_file([[0,1,0,0], [1,1,1,1], [1,0,0,0], [1,1,1,1]], tmp.name)
    >>> with open(tmp.name, "r", encoding="utf-8") as file:
    ...     print(file.read())
    0100
    1111
    1000
    1111
    """
    pass


def find_symmetrical_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Find the symmetrical closure of the {matrix}.
    """
    pass


def find_reflexive_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Find the reflexive closure of the {matrix}.
    """
    pass


def find_transitive_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Find the transitive closure of the {matrix}.
    """
    pass


def split_into_classes(matrix: list[list[int]])-> list[list[int]]:
    """
    Split the relation into equivalence classes.

    >>> split_into_classes([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
    [[0, 1, 2], [3]]
    """
    pass


def is_transitive(matrix: list[list])-> bool:
    """
    Check if the given relation is transitive. Return True if yes, otherwise False.

    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    False
    """
    pass


def find_transitive_number(number: int)-> int:
    """
    Return how many transitive relations are there on relation with n elements.

    :param number: int, Must be <= 4.

    >>> find_transitive_number(0)
    1
    >>> find_transitive_number(2)
    13
    >>> find_transitive_number(3)
    171
    """
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
