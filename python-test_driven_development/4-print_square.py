#!/usr/bin/python3
"""
task 3
"""


def print_quare(size):
    """
    Print square with #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and size < 0:
        raise ValueError("size must be an integer")

    for _ in range(size):
        print('#' * size)
