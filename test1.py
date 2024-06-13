import custom_requests
import requests

url = 'https://643e6d4cc72fda4a0bf6012a.mockapi.io/api/v4/users/test'


def test_1():
    requests.get(url)
    requests.post(url)


def test_2():
    requests.get(url)
    requests.post(url)


if __name__ == '__main__':
    test_1()
    test_2()

    print(f'Logged requests: {custom_requests.get_request_log()}')

