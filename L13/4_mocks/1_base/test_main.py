import unittest
from unittest.mock import Mock
from main import System

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.authorizer = Mock()
        self.system = System(self.authorizer)
        self.request = ...

    def test_schedule_appointment(self):
        self.authorizer.configure_mock(...)
        self.system.schedule_appointment(self.request)
        ...
