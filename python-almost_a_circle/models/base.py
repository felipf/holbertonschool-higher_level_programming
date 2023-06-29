#!/usr/bin/python3
"""
task 0
"""


class Base():
    """
    creating a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initiation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
