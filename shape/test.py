import unittest


class TestRectangle(unittest.TestCase):
    def test_compute_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.compute_area(), 12)

        r = Rectangle(5, 5)
        self.assertEqual(r.compute_area(), 25)

        r = Rectangle(6, 7)
        self.assertEqual(r.compute_area(), 42)
