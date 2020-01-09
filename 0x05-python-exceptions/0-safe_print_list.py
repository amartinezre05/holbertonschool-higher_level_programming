#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for elem in my_list[:x]:
            print("{}".format(elem), end='')
            i += 1
    except IndexError:
        print()
    print()
    return i
