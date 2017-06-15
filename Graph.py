from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, origin, destination, weight):
        self.graph[origin].append([destination, weight])