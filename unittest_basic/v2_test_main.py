import unittest
from main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        result = intersection(1, 2, 5, -1, 2, 3)
        if result != (1, 2):
            raise Exception()

if __name__ == '__main__':
    unittest.main()
