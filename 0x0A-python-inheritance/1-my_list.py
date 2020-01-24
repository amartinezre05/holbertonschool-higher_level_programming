#!/usr/bin/python3
""" Class that print a sorted list """


class MyList(list):
        """ Class My list that inherits from list """
        def print_sorted(self):
                print(sorted(self))
