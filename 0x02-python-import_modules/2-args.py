#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{}: {}".format((i + 1), argv[i + 1]))
    else:
        print("{} arguments.".format(len(argv) - 1))
