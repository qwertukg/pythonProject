import requests
from datetime import datetime, timezone
import inspect
import networkx as nx
import matplotlib.pyplot as plt

request_logs_by_method = {}


def custom_request(self, method, url, **kwargs):
    global request_logs_by_method

    caller_method = inspect.stack()[3].function

    request_info = {
        'order': len(request_logs_by_method.get(caller_method, [])),
        'name': f'{method}:{url}',
        # 'created_at': datetime.now(timezone.utc).isoformat(),
        'caller_method': caller_method
    }

    if caller_method not in request_logs_by_method:
        request_logs_by_method[caller_method] = []
    request_logs_by_method[caller_method].append(request_info)

    original_request = original_request_method
    response = original_request(self, method, url, **kwargs)

    return response


original_request_method = requests.sessions.Session.request
requests.sessions.Session.request = custom_request


def get_request_log():
    global request_logs_by_method

    return request_logs_by_method


def log_to_file(logs):
    return logs
