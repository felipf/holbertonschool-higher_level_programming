#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    bigOne = None
    for comparator in my_list:
        if bigOne is None or bigOne < comparator:
            bigOne = comparator
    return bigOne
