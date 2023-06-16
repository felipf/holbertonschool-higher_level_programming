#!/usr/bin/python3
"""
0-add_integer.py
"""
def add_integer(a, b=98):
    """
    adds integer
    """
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
