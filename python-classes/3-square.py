#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
3-square.py
author: felipf
"""


class Square:
    """
    Square defined
    """

    def __init__(self, size=0):
        """
        size predefined
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        definin' area of square
        """
        return self.__size ** 2