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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        @param
        @width
        @height
        Class rectangle with width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                area1 = rect_1.area()
                area2 = rect_2.area()
                if (area1 >= area2):
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

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
                result += str(self.print_symbol)
            if (i != self.__height - 1):
                result += "\n"
        return result

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        if self:
            Rectangle.number_of_instances -= 1
            del self
            print("Bye rectangle...")
