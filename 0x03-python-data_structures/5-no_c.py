#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for let in my_string:
        if let == 'c' or let == 'C':
            continue
        string += let
    return string
