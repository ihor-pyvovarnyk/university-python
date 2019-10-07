import main
from main import get_slide_titles
from unittest import TestCase
from unittest.mock import Mock

class TestGetSlideTitles(TestCase):
    def setUp(self):
        self.original_requests = main.requests
        self.requests = main.requests = Mock()
        self.requests.get.return_value.json.return_value = {
            'slideshow': {
                'slides': [
                    {'title': 'First title'},
                    {'title': 'Second title'},
                ]
            }
        }

    def tearDown(self):
        main.requests = self.original_requests

    def test_get_slide_titles(self):
        result = get_slide_titles()
        self.assertEqual(result, [
            'First title',
            'Second title',
        ])
