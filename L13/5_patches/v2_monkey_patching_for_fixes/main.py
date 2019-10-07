import requests
...
if __name__ == '__main__':
    requests.get = fixed_version_of_get
    start_app()
