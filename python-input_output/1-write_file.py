#!/usr/bin/python3
""" Module is documented """


def write_file(filename="", text=""):
    """ Function is documented """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
