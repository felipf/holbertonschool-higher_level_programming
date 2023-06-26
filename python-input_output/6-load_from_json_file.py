#!/usr/bin/python3
"""
task 6
"""
import json


def load_from_json_file(filename):
    """
    return rep of obj in string
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
