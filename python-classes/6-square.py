#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
6-square.py
author: felipf
"""


class Square:
    """
    Square defined
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        size predefined
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        definin' area of square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[-1]):
                print("")
            for _ in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
