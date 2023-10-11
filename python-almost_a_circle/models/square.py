#!/usr/bin/python3
"""Class rectangle"""
from rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using a variable-length
        argument list. The arguments should be provided in the order:
        id, width, height, x, y.
        """
        if not args:
            for nm, value in kwargs.items():
                if hasattr(self, nm):
                    setattr(self, nm, value)
        else:
            x = 0
            for attr in args:
                x += 1
                if x == 1:
                    self.id = attr
                elif x == 2:
                    self.size = attr
                elif x == 4:
                    self.x = attr
                elif x == 5:
                    self.y = attr

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
