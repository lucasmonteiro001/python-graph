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

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = dict()

        for vertice in self.vertices:
            visited[vertice] = False

        # Create a queue for BFS
        queue = list()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print s,

            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.vertices[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def printAllPathsUtil(self, source, destination, path, max_stops, compare_function):

        path.append(source)

        # If current vertex is same as destination, then print
        # current path[]
        if source == destination and compare_function(len(path), max_stops):
            print path

        if len(path) > (max_stops + 1):
            return

        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for adjacentVertice in self.vertices[source]:
            self.printAllPathsUtil(adjacentVertice, destination, path, max_stops, compare_function)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()

    def number_of_trips_starting_at_ending_at_max_stops(self, starting_at, ending_at, max_stops):

        def compare_function(path_len, max_number_of_stops):
            return 1 < path_len <= (max_number_of_stops + 1)

        self.printAllPathsUtil(starting_at, ending_at, [], max_stops, compare_function)

    def number_of_trips_starting_at_ending_at_exactly_stops(self, starting_at, ending_at, exactly_stops):

        def compare_function(path_len, number_of_exactly_stops):
            return 1 < path_len == number_of_exactly_stops + 1

        self.printAllPathsUtil(starting_at, ending_at, [], exactly_stops, compare_function)
