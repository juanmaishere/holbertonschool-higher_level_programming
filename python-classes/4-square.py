#!/usr/bin/python3
"""
This module defines a class 'Square' with a size value.
"""


class Square:
    """
    This class represents a square with a given size.

    Attributes:
        size (int): The size of the square.

    Methods:
    __init__(self, size=0): Initializes a new square with the specified size.
    area(self): Calculates the area of the square.

    Properties:
        size (int): Gets or sets the size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square with the specified size.

        :param size: The size of the square.
        :type size: int

        :raises ValueError: If size is negative.
        :raises TypeError: If size is not an integer.
        """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int)):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Area method , that calculates area of square side x side
        """
        return (self.__size * self.__size)
