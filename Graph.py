from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, origin, destination, weight):
        # Initialize adjacent vertices
        if len(self.vertices[origin]) == 0:
            self.vertices[origin] = defaultdict(float)

        self.vertices[origin][destination] = weight
