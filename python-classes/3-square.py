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
        self.__size = size
    
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    
    def size(self):
        return self.__size
    
    def area(self):
        return self.__size ** 2
