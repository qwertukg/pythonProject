from collections import defaultdict
from itertools import groupby
from pprint import pprint
import math
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
                edge_name = action['caller_method']+':'+str(i)
                edges.append((action['name'], actions[i+1]['name'], {'edge_name': edge_name}))
    pprint(edges)
    for from_node, to_node, edge_name in edges:
        G.add_edge(from_node, to_node, **edge_name)

    return G


def draw_graph(G):
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=6)

    grouped_edges = defaultdict(list)
    for edge in G.edges(data=True):
        grouped_edges[(edge[0], edge[1])].append(edge)
    grouped_edges_list = [(key, values) for key, values in grouped_edges.items()]

    for key, edges in grouped_edges_list:
        i = -len(edges) / 2
        for edge in edges:
            rad = i*0.2
            i += 1
            nx.draw_networkx_edges(G, pos, edgelist=[edge], connectionstyle=f'arc3, rad = {rad}', arrows=True)

    for from_node, to_node, edge_data in G.edges(data=True):
        # x1, y1 = pos[from_node]
        # x2, y2 = pos[to_node]
        # x_center = (x1 + x2) / 2
        # y_center = (y1 + y2) / 2
        # rad = i * 0.015
        # i += 1
        #
        # # Вычисление угла наклона ребра
        # dx = x2 - x1
        # dy = y2 - y1
        # angle = math.atan2(dy, dx)
        #
        # # Смещение метки вправо относительно угла
        # offset = rad  # Произвольное смещение
        # label_distance = rad  # Расстояние от ребра
        # x_offset = label_distance * math.cos(angle + math.pi / 2)  # Смещение вправо
        # y_offset = label_distance * math.sin(angle + math.pi / 2)  # Смещение вправо
        #
        # # Отрисовка метки
        # plt.text(x_center + x_offset, y_center + y_offset, edge_data['edge_name'], fontsize=8, ha='center', va='center',
        #          color='red')

        x1, y1 = pos[from_node]
        x2, y2 = pos[to_node]
        label_pos = (x1 + x2) / 2, (y1 + y2) / 2
        plt.text(*label_pos, edge_data['edge_name'], fontsize=8, ha='center', va='center', color='red')

    plt.title('Multi Edges Graph')
    plt.axis('off')
    plt.show()
