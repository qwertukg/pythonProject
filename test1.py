from pprint import pprint

import custom_requests
import requests

from graph import draw_graph, build_dependency_graphs

url1 = 'https://example.com/1'
url2 = 'https://example.com/2'
url3 = 'https://example.com/3'
url4 = 'https://example.com/4'


def test_1():
    requests.get(url1)
    requests.post(url2)


def test_2():
    requests.get(url1)
    requests.post(url2)
    requests.post(url3)


def test_3():
    requests.post(url2)
    requests.get(url3)


def test_4():
    requests.get(url1)
    requests.post(url2)
    requests.get(url3)
    requests.post(url4)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()

    data = custom_requests.get_request_log()
    pprint(data)

    dependency_graphs = build_dependency_graphs(data)

    draw_graph(dependency_graphs)
