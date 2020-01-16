#!/usr/bin/python3
class LockedClass:
    """ prevent the dynamic creation of attr """
    __slots__ = ['first_name']
