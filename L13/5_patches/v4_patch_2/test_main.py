from main import get_slide_titles
from unittest import TestCase
from unittest.mock import patch

class TestGetSlideTitles(TestCase):

    @patch('main.requests')
    def test_get_slide_titles(self, requests):
        requests.get.return_value.json.return_value = {
            'slideshow': {
                'slides': [
                    {'title': 'First title'},
                    {'title': 'Second title'},
                ]
            }
        }
        result = get_slide_titles()
        self.assertEqual(result, [
            'First title',
            'Second title',
        ])
