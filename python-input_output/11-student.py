#!/usr/bin/python3
""" Module is documented """


class Student:
    """ Class is documented """
    def __init__(self, first_name, last_name, age):
        """ Method is documented """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method is documented """
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d

        return class_d

    def reload_from_json(self, json):
        """ Method is documented """
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
