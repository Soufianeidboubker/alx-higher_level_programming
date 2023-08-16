#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sorted()
    for s in list_ord:
        print("{}: {}".format(s, a_dictionary.get(s)))
