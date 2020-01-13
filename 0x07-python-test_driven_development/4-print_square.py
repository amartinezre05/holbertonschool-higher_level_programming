#!/usr/bin/python3
"""
Module print_square
This takes a size.
Type int
"""


def print_square(size):
    """
    Return a square with hashes
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
