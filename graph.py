from itertools import groupby
from pprint import pprint

import networkx as nx
import matplotlib.pyplot as plt


def build_dependency_graphs(data):
    G = nx.MultiDiGraph()

    nodes = set()
    for caller_method, actions in data.items():
        for action in sorted(actions, key=lambda x: x['order']):
            nodes.add(action['name'])
    nodes = tuple(nodes)
    pprint(nodes)
    G.add_nodes_from(nodes)

    edges = []
    for caller_method, actions in data.items():
        for action in sorted(actions, key=lambda x: x['order']):
            i = action['order']
            if i+1 < len(actions):
                edges.append((action['name'], actions[i+1]['name']))
    pprint(edges)
    G.add_edges_from(edges)

    return G, edges


def draw_graph(G, edges):
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos)

    i = 0
    for edge in edges:
        rad = i*0.4
        i += 1
        nx.draw_networkx_edges(G,
                               pos,
                               edgelist=[edge],
                               connectionstyle=f'arc3, rad = {rad}',
                               arrows=True)


    # nx.draw_networkx_edges(G, pos, edgelist=edges, connectionstyle=f'arc3, rad = {0.25}')

    # nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u} -> {v}" for u, v in edges})

    plt.title('Multi Edges Graph')
    plt.axis('off')
    plt.show()
