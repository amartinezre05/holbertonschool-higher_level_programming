#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that inherits of Rectangle """
    def __init__(self, size):
        super().__init__()
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2