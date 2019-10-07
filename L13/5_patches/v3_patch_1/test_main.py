from main import get_slide_titles
from unittest import TestCase
from unittest.mock import patch

class TestGetSlideTitles(TestCase):
    def setUp(self):
        self.patch = patch('main.requests')
        self.requests = self.patch.start()
        self.requests.get.return_value.json.return_value = {
            'slideshow': {
                'slides': [
                    {'title': 'First title'},
                    {'title': 'Second title'},
                ]
            }
        }

    def tearDown(self):
        self.patch.stop()

    def test_get_slide_titles(self):
        result = get_slide_titles()
        self.assertEqual(result, [
            'First title',
            'Second title',
        ])
