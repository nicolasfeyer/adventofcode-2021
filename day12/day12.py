import time
from collections import Counter

import networkx as nx
import matplotlib.pyplot as plt


def read_input() -> nx.Graph:
    graph = nx.Graph()
    with open("data/day12.txt") as file:
    # with open("day12/test.txt") as file:
        from_to = set()
        for l in file:
            from_ = l.split("-")[0].strip()
            to_ = l.split("-")[1].strip()
            from_to.add((from_, to_))

        nodes = set()
        for edge in from_to:
            nodes.add((edge[0], 0, edge[0].isupper()))
            nodes.add((edge[1], 0, edge[1].isupper()))

        graph.add_nodes_from([(n[0], {"visited": n[1], "big": n[2]}) for n in nodes])

        for edge in from_to:
            graph.add_edge(edge[0], edge[1])

    return graph


def find_all_paths_part_one(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph.neighbors(start):
        # if node accepted:
        if node != "start" and (graph.nodes[node]["visited"] != 1 or graph.nodes[node]["big"]):
            graph.nodes[node]["visited"] += 1
            newpaths = find_all_paths_part_one(graph, node, end, path)
            graph.nodes[node]["visited"] -= 1
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths_part_two(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    counts = Counter(n for n in path if n.islower())
    for node in graph.neighbors(start):
        # if node accepted:
        if node != "start" and (sum(counts.values()) <= len(counts) + 1 or graph.nodes[node]["big"]):
            graph.nodes[node]["visited"] += 1
            newpaths = find_all_paths_part_two(graph, node, end, path)
            graph.nodes[node]["visited"] -= 1
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def part_one_two(graph):
    paths = find_all_paths_part_one(graph, "start", "end")
    print(len(paths))
    paths = find_all_paths_part_two(graph, "start", "end")
    print(len(paths))


if __name__ == "__main__":
    t0 = time.time()
    part_one_two(read_input())
    t2 = time.time()
    print("total {total}ms".format(total=t2 - t0))
