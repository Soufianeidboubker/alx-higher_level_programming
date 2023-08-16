#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    ttl= 0

    for s in unique_list:
        ttl += s

    return (ttl)
