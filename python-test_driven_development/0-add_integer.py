#!/usr/bin/python3
def add_integer(a, b=98):
    if (isinstance(a, (int, float))):
        if (isinstance(b, (int, float))):
            b = int(b)
            a = int(a)
            return a + b
        else: raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
