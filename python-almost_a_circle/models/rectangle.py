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
        Initialize width height x and y , public setter and getter.
        :width width of rectangle
        :height height of rectangle
        :x and y position
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
        """ Area que devuelve area """
        return self.__width * self.__height

    def display(self):
        """
        Printea el rectangulo con su width height
        Considerando x y posicion de eje
        """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Str return """
        return f"[Rectangle] {self.id} {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args):
        """Update function to update all value at once"""
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
