#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    cp = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(cp))
