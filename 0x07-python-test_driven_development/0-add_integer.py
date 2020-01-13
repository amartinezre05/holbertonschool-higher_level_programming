#!/usr/bin/python3
"""
Module 0-add_integer.
This takes one or two numbers.
Type int
"""


def add_integer(a, b=98):
    """
    Return the sum of two numbers
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
