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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with the specified size.

        :param size: The size of the square.
        :type size: int

        :raises ValueError: If size is negative.
        :raises TypeError: If size is not an integer.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if (isinstance(value, tuple)):
            if (value[0] >= 0 and value[1] >= 0):
                self.__position = value
        else:
            raise TypeError("position must be \
               a tuple of 2 positive integers")
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

    def my_print(self):
        """
        Prints the square with proper positioning and size.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)