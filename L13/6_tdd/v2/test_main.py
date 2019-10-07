from io import StringIO
from unittest import TestCase
from main import parse_properties

class TestParseProperties(TestCase):
    def test_single_property(self):
        file = StringIO('key=value')
        result = parse_properties(file)
        self.assertEqual(result, {
            'key': 'value'
        })
