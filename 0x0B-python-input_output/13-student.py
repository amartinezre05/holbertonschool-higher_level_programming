#!/usr/bin/python3
"""Class student"""


class Student:
    """a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        a_dict = {}
        for i in attrs:
            try:
                a_dict[i] = self.__dict__[i]
            except:
                pass
        return a_dict

    def reload_from_json(self, json):
        for j in json:
            try:
                setattr(self, j, json[j])
            except:
                pass
