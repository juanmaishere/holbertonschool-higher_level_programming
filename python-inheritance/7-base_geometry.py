#!/usr/bin/python3
"""Declaration of A BaseGeometry Class"""


class BaseGeometry:
    """ Pass Placeholder """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate an itenger"""
        if isinstance(name, str):
            self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
