import unittest
from unittest.mock import sentinel
from main import return_if_condition

class TestReturnIfCondition(unittest.TestCase):
    def test_condition_true(self):
        value = object()
        self.assertEqual(
            value,
            return_if_condition(value, True)
        )

class TestReturnIfCondition2(unittest.TestCase):
    def test_condition_true(self):
        self.assertEqual(
            sentinel.my_value,
            return_if_condition(sentinel.my_value, True)
        )
