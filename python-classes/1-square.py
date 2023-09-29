#!/usr/bin/python3
"""
This module defines a class 'Square' with a size value.
"""

class Square:
    """
    This class represents a square with a given size.
    """

    def __init__(self, size):
        """
        Initializes a new square with the specified size.

        :param size: The size of the square.
        :type size: int
        """
        self.__size = size