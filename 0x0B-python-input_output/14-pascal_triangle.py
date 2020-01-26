#!/usr/bin/python3
def pascal_triangle(n):
    n_list = []
    if n <= 0:
        return n_list
    else:
        for i in range(n):
            for j in range(n):
                n_list.append(1)
                if j == n - 1:
                    num = 1
                    n_list.append(num)
#                else:
#                    num = n_list[j] + n_list[j + 1]
#                    n_list.append(num)
        return n_list
