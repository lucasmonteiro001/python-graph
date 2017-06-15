from collections import defaultdict

inf = float('Inf')


def find_min_index(array, removed_from_queue):
    idx = None

    for i, el in enumerate(array):
        if i not in removed_from_queue:
            idx = i
            break

    for array_index in xrange(1, len(array)):
        if array[array_index] < array[idx] and array_index not in removed_from_queue:
            idx = array_index

    return idx


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

    def get_all_possible_paths_given_compare_function(self, source, destination, path, max_stops, compare_function):

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
            self.get_all_possible_paths_given_compare_function(adjacentVertice, destination, path, max_stops,
                                                               compare_function)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()

    def number_of_trips_starting_at_ending_at_max_stops(self, starting_at, ending_at, max_stops):

        def compare_function(path_len, max_number_of_stops):
            return 1 < path_len <= (max_number_of_stops + 1)

        self.get_all_possible_paths_given_compare_function(starting_at, ending_at, [], max_stops, compare_function)

    def number_of_trips_starting_at_ending_at_exactly_stops(self, starting_at, ending_at, exactly_stops):

        def compare_function(path_len, number_of_exactly_stops):
            return 1 < path_len == number_of_exactly_stops + 1

        self.get_all_possible_paths_given_compare_function(starting_at, ending_at, [], exactly_stops, compare_function)

    # Dijkstra
    def shortest_distance(self, source, destination):

        distance = list()
        queue = list()
        vertice_index_helper = dict()
        index_vertice_helper = dict()
        removed_from_queue = []

        for index, vertice in enumerate(self.vertices):
            if vertice == source:
                distance.append(0)
            else:
                distance.append(inf)

            queue.append(vertice)

            vertice_index_helper[vertice] = index
            index_vertice_helper[index] = vertice

        while len(queue) > 0:
            min_index = find_min_index(distance, removed_from_queue)
            removed_from_queue.append(min_index)
            u = index_vertice_helper[min_index]

            index = queue.index(u)
            del queue[index]

            distance_to_u = distance[vertice_index_helper[u]]

            for v in self.vertices[u]:

                v_index = vertice_index_helper[v]

                distance_to_v = distance[v_index]

                if distance_to_v > distance_to_u + self.vertices[u][v]:
                    distance[v_index] = distance_to_u + self.vertices[u][v]

        return distance[vertice_index_helper[destination]]
