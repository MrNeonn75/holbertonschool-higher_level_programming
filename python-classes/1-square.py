#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module"""


class Square:

    def __init__(self, size):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
