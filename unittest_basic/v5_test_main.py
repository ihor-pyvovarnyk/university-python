import unittest
from main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        result = intersection(1, 2, 5, -1, 2, 3)
        self.assertEqual(result, (1, 2))

    def test_zero_division(self):
        try:
            intersection(1, 1, 2, 1, 1, 3)
        except ZeroDivisionError:
            pass
        else:
            raise Exception()

if __name__ == '__main__':
    unittest.main()
