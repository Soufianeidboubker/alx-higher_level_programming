#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for s in uniq_list:
        num += s

    return (num)
