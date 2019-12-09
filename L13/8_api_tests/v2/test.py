import requests
from unittest import TestCase


class TestHttpServer(TestCase):

    def test_hello(self):
        resp = requests.get('http://localhost:8000/?name=Olena')
        self.assertEqual(resp.json(), {
            'message': f'Hello, Olena!'
        })

    def test_hello_default(self):
        resp = requests.get('http://localhost:8000/')
        self.assertEqual(resp.json(), {
            'message': f'Hello, World!'
        })
