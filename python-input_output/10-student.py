#!/usr/bin/python3
""" Student module """


class Student:
    """ Clase student with attributes """

    def __init__(self, first_name, last_name, age):
        """
        Init class with name last name and age
        :names name of studen
        :age is age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
