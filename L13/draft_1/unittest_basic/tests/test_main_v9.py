import unittest
from main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        result = intersection(1, 2, 5, -1, 2, 3)
        self.assertEqual(result, (1, 2))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            intersection(1, 1, 2, 1, 1, 3)
