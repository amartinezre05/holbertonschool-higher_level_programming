#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    number_lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            number_lines += 1
        if nb_lines <= 0 or nb_lines > number_lines:
            print(f.read(), end='')
        else:
            print(f.read(nb_lines), end='')
