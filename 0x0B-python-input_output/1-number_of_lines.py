#!/usr/bin/python3
def number_of_lines(filename=""):
    number_lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            number_lines += 1
    return number_lines
