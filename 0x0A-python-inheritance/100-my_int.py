#!/usr/bin/python3
""" Class MyInt """


class MyInt(int):
    """ Class that inherits from int """
    def __eq__(self, value):
        return int(self) != int(value)

    def __ne__(self, value):
        return int(self) == int(value)
