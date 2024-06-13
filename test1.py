import requests

url = 'https://643e6d4cc72fda4a0bf6012a.mockapi.io/api/v4/users/test'


def custom_request(self, method, url, **kwargs):
    print(f'Performing {method} request to {url} with kwargs={kwargs}')

    original_request = original_request_method

    return original_request(self, method, url, **kwargs)


original_request_method = requests.sessions.Session.request

requests.sessions.Session.request = custom_request

if __name__ == '__main__':
    response = requests.get(url)
    print(response.text)

    response = requests.post(url)
    print(response.text)
