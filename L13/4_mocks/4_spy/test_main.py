import unittest
from unittest.mock import Mock
from main import Authorizer, System

class AuthorizerSpy:
    def __init__(self):
        self.authorized_was_called = False

    def authorize(self, username, password):
        self.authorized_was_called = True
        return True

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.authorizer = AuthorizerSpy()
        self.system = System(self.authorizer)
        ...

    def test_schedule_appointment(self):
        self.system.schedule_appointment(self.request)
        self.assertTrue(self.authorizer.authorized_was_called)
        ...

class TestSystem2(unittest.TestCase):
    def setUp(self):
        self.authorizer = Mock(return_value=True)
        self.system = System(self.authorizer)
        self.request = Mock(username='josh', password='123456')

    def test_successful_schedule_appointment(self):
        self.system.schedule_appointment(self.request)
        self.assertTrue(self.authorizer.authorize.called)
        ...

