#!/usr/bin/python3

"""
    The ``1. Base class`` module
"""
import json


class Base:
    """
        Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Function that returns the JSON string representation
            of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Function that returns the list of the JSON string
            representation json_string
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Function that writes the JSON string
            representation of list_objs to a file
        """
        list_dictionaries = None
        if list_objs is not None:
            list_dictionaries = []
            for i in list_objs:
                list_dictionaries.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))
        f.close()

    @classmethod
    def create(cls, **dictionary):
        """
            Function that returns an instance with all
            attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Square:
            new_instance = Square(3)
        if cls is Rectangle:
            new_instance = Rectangle(3, 5)
        try:
            new_instance.update(**dictionary)
        except Exception:
            pass
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
            Function that returns a list of instances
        """
        new_list = []
        try:
            with open("{}.json".format(cls.__name__),
                      "r", encoding="utf-8") as f:
                read_data = f.read()
                list_json = cls.from_json_string(read_data)
                try:
                    for dictionary in list_json:
                        new_list.append(cls.create(**dictionary))
                except Exception:
                    pass
            f.close()
        except Exception:
            pass
        finally:
            return new_list
