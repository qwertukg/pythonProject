import requests
import datetime

request_log = []


def custom_request(self, method, url, **kwargs):
    global request_log

    request_info = {
        'order': len(request_log) + 1,
        'name': f'{method}:{url}',
        'createdAt': datetime.datetime.utcnow().isoformat() + 'Z'
    }

    request_log.append(request_info)

    original_request = original_request_method
    response = original_request(self, method, url, **kwargs)

    return response


original_request_method = requests.sessions.Session.request

requests.sessions.Session.request = custom_request


def get_request_log():
    global request_log
    return request_log
