from main import get_slide_titles
from unittest import TestCase
from unittest.mock import patch, MagicMock

@patch('main.requests', MagicMock(**{
    'get.return_value.json.return_value': {
        'slideshow': {
            'slides': [
                {'title': 'First title'},
                {'title': 'Second title'},
            ]
        }
    }
}))
class TestGetSlideTitles(TestCase):
    def test_get_slide_titles(self):
        result = get_slide_titles()
        self.assertEqual(result, [
            'First title',
            'Second title',
        ])
