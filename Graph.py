from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, origin, destination, weight):
        # Initialize adjacent vertices
        if len(self.vertices[origin]) == 0:
            self.vertices[origin] = defaultdict(float)

        self.vertices[origin][destination] = weight

    def find_route_distance_among(self, vertices, initial_distance=0.0):

        if len(vertices) <= 1:
            return initial_distance

        origin = vertices[0]
        destination = vertices[1]

        # Verify if edge exists
        if destination not in self.vertices[origin]:
            return "NO SUCH ROUTE"

        distance = self.vertices[origin][destination]

        return self.find_route_distance_among(vertices[1:], distance + initial_distance)
