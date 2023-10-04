#!/usr/bin/python3
"""Declaration of A BaseGeometry Class"""


class BaseGeometry:
    """ Pass Placeholder """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        if isinstance(value, int):
            if value > 0:
                return self.name
            else:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")