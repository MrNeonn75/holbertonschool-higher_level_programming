#!/usr/bin/python3

"""
    The ``2. First Rectangle`` module
"""


from models.base import Base


class Rectangle(Base):
    """
        Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set the value for width
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
            Set the value for height
        """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """
            Set the value for x
        """
        self.validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """
            Set the value for y
        """
        self.validator("y", value, True)
        self.__y = value

    def validator(self, attribute_name, value, can_be_zero=False):
        """
            Checks the value valid or not
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute_name))
        if not can_be_zero and value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))
        if can_be_zero and value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))

    def area(self):
        """
            Function that returns area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints Rectangle using # sign
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
            Returns class in this format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        result = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y,
                   self.__width, self.__height)
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
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        else:
            try:
                self.id = kwargs['id']
            except Exception:
                pass
            try:
                self.width = kwargs['width']
            except Exception:
                pass
            try:
                self.height = kwargs['height']
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
            representation of a Rectangle
        """
        new_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
        return new_dict
