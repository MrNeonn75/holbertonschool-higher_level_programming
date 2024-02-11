#!/usr/bin/python3
""" Module is documented """


class Student:
    """ Class is documented """
    def __init__(self, first_name, last_name, age):
        """ Method is documented """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method is documented """
        return self.__dict__
