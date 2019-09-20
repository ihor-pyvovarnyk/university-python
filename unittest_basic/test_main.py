import unittest
from main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        print(intersection(1, 2, 3, -4, 1, -6))


if __name__ == '__main__':
    unittest.main()
