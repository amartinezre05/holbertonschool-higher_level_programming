#!/usr/bin/python3
"""
Module text_indentation
Takes two characters . and ?
and print 2 new lines after them
"""


def text_indentation(text):
    """
    Return the text with the new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            text[i] = text[i] +'\n'+'\n'
    print(text)
