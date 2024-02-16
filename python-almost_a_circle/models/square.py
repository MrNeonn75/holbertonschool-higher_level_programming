#!/usr/bin/python3

"""
    The ``Square`` module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """
            Set the side size of Square
        """
        self.width = value
        self.height = value

    def __str__(self):
        result = "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)
        return result

    def update(self, *args, **kwargs):
        """
            Function that assigns an
            argument to each attribute
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            try:
                self.id = kwargs['id']
            except Exception:
                pass
            try:
                self.width = kwargs['size']
            except Exception:
                pass
            try:
                self.height = kwargs['size']
            except Exception:
                pass
            try:
                self.x = kwargs['x']
            except Exception:
                pass
            try:
                self.y = kwargs['y']
            except Exception:
                pass

    def to_dictionary(self):
        """
            Function that returns the dictionary
            representation of a Square
        """
        new_dict = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
        return new_dict
