import unittest
from incorrect_main import intersection

class TestMain(unittest.TestCase):

    def test_intersection(self):
        result = intersection(1, 2, 5, -1, 2, 3)
        if (1, 2) != result:
            raise Exception()
