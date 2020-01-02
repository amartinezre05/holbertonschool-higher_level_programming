#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    for l in range(len(str)):
        if l == n:
            continue
        else:
            str_copy += str[l]
    return str_copy
