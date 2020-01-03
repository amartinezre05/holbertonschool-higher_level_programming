#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{}".format(len(argv) - 1))
    elif len(argv) > 1:
        suma = 0
        for i in range(len(argv) - 1):
            suma += int(argv[i + 1])
        print("{}".format(suma))
