import requests

def get_slide_titles():
    response = requests.get('http://httpbin.org/json').json()
    return [
        slide['title'] for slide in response['slideshow']['slides']
    ]
