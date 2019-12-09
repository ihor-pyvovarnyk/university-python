from urllib.error import HTTPError
from urllib.request import urlopen
from unittest import TestCase


class TestHttpServer(TestCase):

    def test_root(self):
        resp = urlopen('http://localhost:8000')
        self.assertEqual(200, resp.code)

    def test_current_file(self):
        resp = urlopen('http://localhost:8000/test.py')
        self.assertEqual(200, resp.code)
        with open(__file__, 'r') as f:
            self.assertEqual(f.read(), resp.fp.read().decode())

    def test_missing_path(self):
        with self.assertRaises(HTTPError) as context:
            urlopen('http://localhost:8000/missing_path')
        self.assertEqual(404, context.exception.code)
