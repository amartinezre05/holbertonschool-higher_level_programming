#!/usr/bin/python3
""" Class Square """


class Square:
    """ Square class with size """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * '#')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        m = "position must be a tuple of 2 positive integers"
        for i in value:
            if i < 0:
                raise TypeError(m)
            else:
                if len(value) != 2 or type(value) != tuple:
                    raise TypeError(m)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for j in range(self.__position[0]):
                print(" ", end='')
            for i in range(self.__size):
                print(self.__size * '#')
