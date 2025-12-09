#!/usr/bin/python3
"""
This module defines a Square class with private attribute and public method
"""


class Square:
    """
    This class creates a square with assigned size
    Attributes:
        __size(int): defines the size of square's sides
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
