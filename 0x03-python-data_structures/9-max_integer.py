#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    small = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > small:
            small = my_list[i]

    return (small)
