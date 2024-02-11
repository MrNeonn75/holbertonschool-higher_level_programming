#!/usr/bin/python3
""" Module is documented """


from json import dumps
""" Module is documented """


def save_to_json_file(my_obj, filename):
    """ Function is documented """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
