#!/usr/bin/python3
"""
task 2
"""


def append_write(filename="", text=""):
    """
    appends str at end of file and returns n char
    """
    with open(filename, mode='a', encoding='utf-8') as appfile:
        appfile.write(text)
    return len(text)
