import unittest
from shape import Rectangle


class TestRectangle(unittest.TestCase):
    def test_compute_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.compute_area(), 12)

        r = Rectangle(5, 5)
        self.assertEqual(r.compute_area(), 25)

        r = Rectangle(6, 7)
        self.assertEqual(r.compute_area(), 42)

    def test_get_set_width(self):
        r = Rectangle(3, 4)
        r.set_width(6)
        self.assertEqual(r.get_width(), 6)

        r = Rectangle(5, 5)
        r.set_width(2)
        self.assertEqual(r.get_width(), 2)

        r = Rectangle(7, 5)
        r.set_width(3)
        self.assertEqual(r.get_width(), 3)
        r.set_width(8)
        self.assertEqual(r.get_width(), 8)

    def test_get_set_height(self):
        r = Rectangle(3, 4)
        r.set_height(2)
        self.assertEqual(r.get_height(), 2)

        r = Rectangle(5, 5)
        r.set_height(4)
        self.assertEqual(r.get_height(), 4)

        r = Rectangle(7, 5)
        r.set_height(4)
        self.assertEqual(r.get_height(), 4)
        r.set_height(8)
        self.assertEqual(r.get_height(), 8)
