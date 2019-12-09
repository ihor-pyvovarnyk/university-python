from flask_testing import TestCase
from .app import app


class BaseTestCase(TestCase):
    def create_app(self):
        return app


class TestHttpServer(BaseTestCase):

    def test_hello(self):
        resp = self.client.get('/', query_string='name=Olena')
        self.assertEqual(resp.json, {
            'message': f'Hello, Olena!'
        })

    def test_hello_default(self):
        resp = self.client.get('/')
        self.assertEqual(resp.json, {
            'message': f'Hello, World!'
        })
