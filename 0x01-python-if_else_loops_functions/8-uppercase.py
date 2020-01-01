#!/usr/bin/python3
def uppercase(str):
    for l in range(len(str)):
        c = ord(str[l])
        if c > 96 and c < 123:
            c = c - 32
        print("{}".format(chr(c)), end="")
    print()
