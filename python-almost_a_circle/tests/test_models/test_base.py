#!/usr/bin/python3

"""
    Tests for Almost A circle module - Base Class
"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_id_checker(self):
        # None case
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base(None)
        self.assertEqual(b1.id, 2)

        # Positive integer case
        b2 = Base(3)
        self.assertEqual(b2.id, 3)

        b2 = Base(4)
        self.assertEqual(b2.id, 4)

        # Negative integer case
        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

        b3 = Base(-6)
        self.assertEqual(b3.id, -6)

        # String case
        b4  = Base("Saul Goodman was here.")
        self.assertEqual(b4.id, "Saul Goodman was here.")

        b4 = Base("If you don't like Kanye, I don't like you.")
        self.assertEqual(b4.id, "If you don't like Kanye, I don't like you.")

    def test_json_converters(self):
        """
            Tests for to_json_string method
        """
        # None case
        json_string_1 = Base.to_json_string(None)
        self.assertEqual(json_string_1, "[]")

        # Empty list case
        json_string_2 = Base.to_json_string([])
        self.assertEqual(json_string_2, "[]")

        # Ordinary Dictionary case
        json_string_3 = Base.to_json_string([{"id": 1}])
        self.assertEqual(json_string_3, '[{"id": 1}]')

        """
            Tests for from_json_string method
        """
        # None case
        list_1 = Base.from_json_string(None)
        self.assertEqual(list_1, [])

        # Empty list string case
        list_2 = Base.from_json_string("[]")
        self.assertEqual(list_2, [])

        # Ordinary json string case
        list_3 = Base.from_json_string('[{"id": 2}]')
        self.assertEqual(list_3, [{"id": 2}])
