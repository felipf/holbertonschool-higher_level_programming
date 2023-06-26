#!/usr/bin/python3
"""
task 7
"""


class BaseGeometry():
    """
    class geo
    """
    def area(self):
        """
        exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(name + "must be an integer")
        if value <= 0:
            raise ValueError(name + "must be greater than 0")
