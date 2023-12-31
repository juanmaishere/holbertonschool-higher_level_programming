#!/usr/bin/python3
"""
Definition of a class Rectangle with pass placeholder
"""


class Rectangle:
    """
    Class rectangule with
    :width: widht of rectangle
    :height rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new square with the specified size.

        :param size: The size of the square.
        :type size: int
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
