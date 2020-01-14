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
    new_str = ""
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new_str += text[i]+'\n'+'\n'
            i += 1
        else:
            c = text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':'
            if c and text[i] == ' ':
                continue
            else:
                new_str += text[i]
    print(new_str, end="")
