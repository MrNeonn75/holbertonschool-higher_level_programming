#!/usr/bin/python3

"""
    Tests for Almost a circle module - Rectangle Class
"""


import unittest
from unittest.mock import patch

import os
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        """ Creating instances for testing """
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.r3 = Rectangle(1, 1, 1, 1, 1)

        self.new_dictionary = {"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}
        self.r1_list = [self.r1]

    def test_rectangle(self):
        # Only height and width initialization
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        # Initalization of all attributes
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

        # Type error cases
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("2", 3)
        with self.assertRaises(TypeError):
            Rectangle(4, "5")
        with self.assertRaises(TypeError):
            Rectangle(6, 7, "8")
        with self.assertRaises(TypeError):
            Rectangle(9, 10, 11, "12")

        # Value error cases
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(3, -4)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(6, 0)
        with self.assertRaises(ValueError):
            Rectangle(7, 8, -9)
        with self.assertRaises(ValueError):
            Rectangle(10, 11, 12, -13)

    """ Method testing: area() """
    def test_area(self):
        self.assertEqual(self.r2.area(), 2)

    """ Method testing: __str__ """
    def test_str(self):
        self.assertEqual(str(self.r2), "[Rectangle] (5) 3/4 - 1/2")

    """ Method testing: display """
    def test_display(self):
        output = "#\n"
        with patch("sys.stdout", new=StringIO()) as out:
            self.r1.display()
            self.assertEqual(out.getvalue(), output)
        output = "\n #\n"

        with patch("sys.stdout", new=StringIO()) as out:
            self.r3.display()
            self.assertEqual(out.getvalue(), output)

    """ Method testing: to_dictionary """
    def  test_to_dictionary(self):
        self.assertEqual(self.r2.to_dictionary(), {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4})

    """ Method testing: update """
    def test_update(self):
        self.r1.update(1, 2, 3, 4, 5)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 4/5 - 2/3")

    """ Method testing: create """
    def test_create(self):
        new_instance = Rectangle.create(**self.new_dictionary)
        self.assertEqual(str(new_instance), "[Rectangle] (1) 1/1 - 1/1")

    """ Method testing: save_to_file"""
    def test_save_to_file_case_1(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
    
    def test_save_to_file_case_2(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_case_3(self):
        Rectangle.save_to_file([Rectangle(1, 2, id=1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    """ Method testing: load_from_file """
    def test_load_from_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

        Rectangle.save_to_file(self.r1_list)
        self.assertEqual(self.r1_list[0].__str__(), Rectangle.load_from_file()[0].__str__())


    def tearDown(self):
        """ Method that execute before other methods. """
        try:
            os.remove("Rectangle.json")
        except:
            pass
