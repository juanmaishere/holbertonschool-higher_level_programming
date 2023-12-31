#!/usr/bin/python3
""" Summary """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts a list of dict to json respresentation
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        
        for obj in list_objs:
            with open(filename, "w") as file:
                json_str = cls.to_json_string(obj)
                file.write(json_str)
