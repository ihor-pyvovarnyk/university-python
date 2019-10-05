import unittest
from unittest.mock import Mock
from main import Authorizer, System

class AuthorizerStub:
    def authorize(self, username, password):
        return True

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.authorizer = AuthorizerStub()
        self.system = System(self.authorizer)

    def test_successful_schedule_appointment(self):
        self.system.schedule_appointment(self.request)
        ...  # перевірки для логіки при успішній авторизації


class TestSystem2(unittest.TestCase):
    def setUp(self):
        self.authorizer = Mock()
        self.system = System(self.authorizer)
        self.request = Mock(username='josh', password='123456')

    def test_successful_schedule_appointment(self):
        self.authorizer.authorize.return_value = True
        self.system.schedule_appointment(self.request)
        ...  # перевірки для логіки при успішній авторизації

    def test_failed_schedule_appointment(self):
        self.authorizer.authorize.return_value = False
        self.system.schedule_appointment(self.request)
        ...  # перевірки для логіки при неуспішній авторизації
