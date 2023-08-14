#!/usr/bin/python3
# 11-delete_at.py

def delete_at(nw_list=[], idx=0):
    if idx >= 0 and idx < len(nw_list):
        del nw_list[idx]
    return (nw_list)
