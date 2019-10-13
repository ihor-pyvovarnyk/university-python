from io import StringIO
from unittest import TestCase
from main import parse_properties

class TestParseProperties(TestCase):
    def test_single_property(self):
        file = StringIO('key=value')
        result = parse_properties(file)
        self.assertEqual(result, {'key': 'value'})

    def test_multiple_properties(self):
        file = StringIO(
            'key1=value1\nkey2=value2'
        )
        result = parse_properties(file)
        self.assertEqual(result, {
            'key1': 'value1',
            'key2': 'value2',
        })

    def test_comments(self):
        file = StringIO(
            'key=value\n# comment'
        )
        result = parse_properties(file)
        self.assertEqual(result, {
            'key': 'value'
        })