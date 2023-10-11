#!/usr/bin/python3
"""Class rectangle"""
from base import Base


class Rectangle(Base):
    """
    Clase rectangulo
    con getter y setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle with width, height, x, and y coordinates.
        :param width: Width of the rectangle (must be a positive integer).
        :param height: Height of the rectangle (must be a positive integer).
        :param x: X-coordinate of the top-left corner non-negative integer).
        :param y: Y-coordinate of the top-left corner non-negative integer).
        :param id: Identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
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
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        area method to return area
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle as a series of
        characters with proper positioning
        """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        str method to return string
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

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
                    self.width = attr
                elif x == 3:
                    self.height = attr
                elif x == 4:
                    self.x = attr
                elif x == 5:
                    self.y = attr

    def to_dictionary(self):
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
