#!/usr/bin/python3
"""
Definition of a class Rectangle with pass placeholder
"""


class Rectangle:
    """
    @param
    @width
    @height

    Class rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
        @param
        @width
        @height
        Class rectangle with width and height
        """
        self.width = width
        self.height = height

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            d = self.__height * 2
            c = self.__width * 2
            return d + c

    def __str__(self):
        """
        String function for returning form
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            if (i != self.__height - 1):
                result += "\n"
        return result
