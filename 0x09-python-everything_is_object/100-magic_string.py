#!/usr/bin/python3
def magic_string():
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
magic_string.n = getattr(magic_string, 'n', 0) + 1
