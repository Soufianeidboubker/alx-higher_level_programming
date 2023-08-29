#!/usr/bin/python3
def search_replace(my_list, search, replace):
    old_list = list(map(lambda y: replace if y == search else y, my_list))
    return (old_list)
