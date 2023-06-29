#!/usr/bin/python3
"""
task 1
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class created
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def set_width(self, value):
        self.__width = value

    @height.setter
    def set_height(self, value):
        self.__height = value

    @x.setter
    def set_x(self, value):
        self.__x = value

    @y.setter
    def set_y(self, value):
        self.__y = value
