#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.cp()
    list_keys = list(new_dir.keys())

    for s in list_keys:
        new_dir[s] *= 2

    return (new_dir)
