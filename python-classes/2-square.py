#!/usr/bin/python3
"""
This module defines a class 'Square' with a size value.
"""


class Square:
    """
    This class represents a square with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the specified size.

        :param size: The size of the square.
        :type size: int

        :raises ValueError: If size is negative.
        :raises TypeError: If size is not an integer.
        """
        if (isinstance(size, int)):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
