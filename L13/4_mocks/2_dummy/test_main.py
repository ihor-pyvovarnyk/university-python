import unittest
from main import Authorizer, System

class TestSystem(unittest.TestCase):
    def setUp(self):
        ...
        self.system = System(authorizer=None)
        ...
        self.system = System(authorizer=object())
        ...
        from unittest.mock import sentinel
        self.system = System(authorizer=sentinel.authorizer)
        ...
    ...
