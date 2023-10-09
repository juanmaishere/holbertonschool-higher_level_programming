#!/usr/bin/python3
""" Summary """


class Base:
    """
    Clase base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Id asignado o incrementado por instancias
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
