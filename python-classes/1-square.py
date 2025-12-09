#!/usr/bin/python3
"""
This module defines a Square class with private attribute
"""


class Square:
    """
    This is a class to represent a square by its sizes.
    Attributes:
        __size(int): The size of square's sizes
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
