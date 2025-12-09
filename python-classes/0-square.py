#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""
class Square:
    """
    A class to represent a square.
    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance.
        Parameters:
        size (int): The size of the square's sides.
        """
        self.__size = size
