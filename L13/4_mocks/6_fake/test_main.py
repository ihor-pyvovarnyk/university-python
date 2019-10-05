import unittest
from unittest.mock import Mock
from main import Authorizer, System

class AuthorizerFake:
    def __init__(self):
        self._authorized_was_called = False

    def authorize(self, username, password):
        return username == 'Bob'

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.authorizer = AuthorizerFake()
        self.system = System(self.authorizer)
        ...

    def test_schedule_appointment_for_bob(self):
        self.system.schedule_appointment(self.request)
        ...

class TestSystem2(unittest.TestCase):
    def setUp(self):
        self.authorizer = Mock()
        self.system = System(self.authorizer)
        self.request = Mock(username='josh', password='123456')

    def test_schedule_appointment_for_bob(self):
        self.authorizer.side_effect = \
            lambda username, password: username == 'Bob'
        self.system.schedule_appointment(self.request)
        ...

