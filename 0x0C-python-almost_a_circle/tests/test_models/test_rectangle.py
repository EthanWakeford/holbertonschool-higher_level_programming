#!/usr/bin/python3
"""test file for rectangle.py"""
from models.rectangle import Rectangle
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """rectangle class testing"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').rectangle.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test__str__(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/1 - 1/1')
        r1 = Rectangle(5, 3, 1, 6, 100)
        self.assertEqual(r1.__str__(), '[Rectangle] (100) 1/6 - 5/3')

    def a_test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)

    def test_errors(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 'f')
        with self.assertRaises(TypeError):
            r1 = Rectangle('d', 3)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 'sadf', 5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 'dsf')
        with self.assertRaises(TypeError):
            r1 = Rectangle(None)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -2, 45)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 4, -6)

    def test_area(self):
        r1 = Rectangle(3, 3)
        self.assertEqual(r1.area(), 9)
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_display(self):
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")
        r1 = Rectangle(3, 2, 1, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 3/1 - 2/10')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 1/3 - 4/2')
        with self.assertRaises(TypeError):
            r1.update(width="string")
        with self.assertRaises(ValueError):
            r1.update(width=-5)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 13, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        r2.update(**(r1.to_dictionary()))
        self.assertEqual(r2.__str__(), '[Rectangle] (13) 1/9 - 10/2')
        self.assertIsNot(r1, r2)
