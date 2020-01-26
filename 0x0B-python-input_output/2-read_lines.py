#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    number_lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            number_lines += 1
        if nb_lines <= 0 or nb_lines > number_lines:
            f.seek(0)
            print(f.read(), end='')
        else:
            f.seek(0)
            i = 0
            for line in f:
                if i < nb_lines: 
                    print(line, end='')
                i += 1
