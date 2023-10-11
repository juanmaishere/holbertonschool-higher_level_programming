#!/usr/bin/python3
"""Class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Clase square inherits from rectangle
    size is width and height
    x and y position
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init , super class recieves size
        x and y , from rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str returns string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
