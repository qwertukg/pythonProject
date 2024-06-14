from pprint import pprint

import custom_requests
import requests

from graph import draw_graph, build_dependency_graphs

url1 = 'https://example.com/first'
url2 = 'https://example.com/second'
url3 = 'https://example.com/third'


def test_1():
    requests.get(url1)
    requests.post(url2)


def test_2():
    requests.get(url1)
    requests.post(url2)
    requests.post(url3)

def test_3():
    requests.post(url2)
    requests.post(url3)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()

    data = custom_requests.get_request_log()
    pprint(data)

    dependency_graphs, edges = build_dependency_graphs(data)

    draw_graph(dependency_graphs, edges)

