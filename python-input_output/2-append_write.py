#!/usr/bin/python3
"""
task 2
"""


def write_file(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as appfile:
        appfile.write(text)
    return len(text)
