#!/usr/bin/python3
"""Declaration of A Rectangle Class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square rectangle inherit class"""

    def __init__(self, size):
        """
        Init For the Square
        :Area Returns area
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Area Method Func for square
        """
        return self.__size * self.__size
    
    def __str__(self):
        """
        str returns square width and height
        """
        return f"[Square] {self.__size}/{self.__size}"