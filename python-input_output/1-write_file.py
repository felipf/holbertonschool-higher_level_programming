#!/usr/bin/python3
"""
task 1
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as Wfile:
        Wfile.write(text)
    return len(text)
