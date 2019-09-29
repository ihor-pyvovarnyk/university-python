import unittest
from incorrect_main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        result = intersection(1, 2, 5, -1, 2, 3)
        self.assertEqual((1, 2), result)

    def test_parallel_lines(self):
        with self.assertRaises(ZeroDivisionError):
            intersection(1, 1, 2, 1, 1, 3)

if __name__ == '__main__':
    unittest.main()
