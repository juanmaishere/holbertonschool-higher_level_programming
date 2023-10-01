#!/usr/bin/python3
import test
"""
add 2 integers
"""


def add_integer(a, b=98):
    """
    Add two numbers, casting them to integers if they are floats.

    :param a: The first number.
    :param b: The second number (default is 98).
    :return: The sum of the two numbers.

    >>> add_integer(10, 20)
    30

    >>> add_integer(15.5, 5)
    20

    >>> add_integer(7, 3.5)
    10

    >>> add_integer(3.2, 4.8)
    8

    >>> add_integer(10, "not_an_integer")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    >>> add_integer("not_an_integer", 10)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if (isinstance(a, (int, float))):
        if (isinstance(b, (int, float))):
            b = int(b)
            a = int(a)
            return a + b
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
