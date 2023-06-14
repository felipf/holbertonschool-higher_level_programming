#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
5-square.py
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

    @property
    def size(self):
        """
        retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        define value errors
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        definin' area of square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            for size in range(self.__size):
                print("#" * self.__size)
