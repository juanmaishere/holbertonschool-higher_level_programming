#!/usr/bin/python3
"""Declaration of A Rectangle Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square rectangle inherit class"""
    
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * 2
