#!/usr/bin/python3
"""
task 5
"""
import json


def save_to_json_string(my_obj, filename):
    """
    return rep of obj in string
    """
    with open(filename, mode='w') as j_son:
        json.dump(my_obj, j_son)
