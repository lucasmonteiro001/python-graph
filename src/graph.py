"""Module responsible for the graph structure"""

from collections import defaultdict

# Infinit value
INF = float('Inf')


def find_min_index(array, removed_from_queue):
    """
    Find the index that contains the minimum value that is not in the #removed_from_queue
    :param array: array with values
    :param removed_from_queue:
    :return: index of the minimum value in the array
    """
    idx = None

    # Gets the first available and valid index
    for i, el in enumerate(array):
        if i not in removed_from_queue:
            idx = i
            break

    # Discover the index of the minimum value
    for array_index in xrange(1, len(array)):
        if array[array_index] < array[idx] and array_index not in removed_from_queue:
            idx = array_index

    return idx


class Graph(object):
    """
    Class that represents a graph
    """

    def __init__(self):
        # Initialize the list of vertices
        self.vertices = defaultdict(list)

    def add_edge(self, origin, destination, weight):
        """
        Add an edge to the graph
        :param origin: vertice of origin
        :param destination: vertice of destination
        :param weight: weight of the edge
        :return: None
        """
        # Initialize adjacent vertices
        if len(self.vertices[origin]) == 0:
            self.vertices[origin] = defaultdict(int)

        self.vertices[origin][destination] = weight

    def find_route_distance_among_vertices(self, vertices, initial_distance=0):
        """
        Given a list of #vertices, find the distance from vertice[0] to vertice[len(vertice)]
        :param vertices: list of vertices, e.g (["A", "B", "C"])
        :param initial_distance: initial value for distance
        :return:
        """

        # If there is only one vertice, return the initial distance
        if len(vertices) <= 1:
            return initial_distance

        origin = vertices[0]
        destination = vertices[1]

        # Verify if edge exists
        if destination not in self.vertices[origin]:
            return "NO SUCH ROUTE"

        # Get direct distance between origin and destination
        distance = self.vertices[origin][destination]

        return self.find_route_distance_among_vertices(vertices[1:], distance + initial_distance)

    def get_all_possible_paths(self, source, destination, path, max_stops, compare_function,
                               cumulative_result):
        """
        Get all possible paths
        :param source: origin
        :param destination: destination
        :param path: path
        :param max_stops: max number of stops
        :param compare_function: function that represents stop condition
        :param cumulative_result: cumulative result of the lenght's path
        :return: total number of possible paths
        """

        # add source to the path
        path.append(source)

        # If current vertice is the same of destination
        if source == destination and compare_function(len(path), max_stops):
            cumulative_result += 1

        # Path cant be greater than max_stops + 1
        if len(path) > (max_stops + 1):
            return cumulative_result

        # Loop through all adjacent vertices
        for adjacentVertice in self.vertices[source]:
            cumulative_result = self.get_all_possible_paths(
                adjacentVertice, destination, path, max_stops, compare_function, cumulative_result)

            # Remove vertice from the path
            path.pop()

        return cumulative_result

    def get_all_possible_paths_within_distance(self, source, destination, path, max_distance,
                                               current_distance, cumulative_result):
        """
        Get all possible paths within a distance
        :param source: origin
        :param destination: destination
        :param path: path
        :param max_distance: max distance that may be in path
        :param current_distance: current distance
        :param cumulative_result: cumulative result of the lenght's path
        :return: total number of possible paths
        """

        path.append(source)

        # If path is valid
        if source == destination and current_distance < max_distance and len(path) > 1:
            cumulative_result += 1

        # If it's not possible to add more vertices to the path
        if current_distance >= max_distance:
            return cumulative_result

        # If current vertice is not destination
        # Recur for all the vertices adjacent to this vertice
        for adjacentVertice in self.vertices[source]:
            cumulative_result = self.get_all_possible_paths_within_distance(
                adjacentVertice, destination, path, max_distance,
                current_distance + self.vertices[source][adjacentVertice], cumulative_result)

            # Remove vertice from the path
            path.pop()

        return cumulative_result

    def get_total_trips_max_stops(self, origin, destination, max_stops):
        """
        Get the total number of trips between #origin vertice and #destination vertice
        that have #max_stops stops at the most
        :param origin: origin vertice
        :param destination: destination vertice
        :param max_stops: number of stops
        :return: total number of trips that fit the criteria
        """

        def compare_function(path_len, max_number_of_stops):
            """
            Function that checks if lenght's path is valid
            :param path_len:
            :param max_number_of_stops:
            :return:
            """
            return 1 < path_len <= (max_number_of_stops + 1)

        return self.get_all_possible_paths(origin, destination, [], max_stops, compare_function, 0)

    def get_total_trips_exact_stops(self, origin, destination, exactly_stops):
        """
        Get the total number of trips between #origin vertice and #destination vertice
        that have exactly #exactly_stops stops
        :param origin: origin vertice
        :param destination: destination vertice
        :param exactly_stops: number of stops
        :return: total number of trips that fit the criteria
        """

        def compare_function(path_len, number_of_exactly_stops):
            """
            Function that checks if lenght's path is valid
            :param path_len:
            :param number_of_exactly_stops:
            :return:
            """
            return 1 < path_len == number_of_exactly_stops + 1

        return self.get_all_possible_paths(origin, destination, [], exactly_stops,
                                           compare_function, 0)

    def get_total_trips_distance_less_than(self, origin, destination, distance):
        """
        Get the total number of trips between #origin vertice and #destination vertice
        that have less than #distance in distance
        :param origin: origin vertice
        :param destination: destination vertice
        :param distance: max distance
        :return: total number of trips that fit the criteria
        """

        return self.get_all_possible_paths_within_distance(origin, destination, [], distance, 0, 0)

    def get_shortest_distance(self, origin, destination):
        """
        Get the shortest distance between #origin and #destination
        This algorithm is based on DIJKSTRA ALGORITHM to find the
        shortest distance between two nodes in a graph with positive edges
        :param origin: origin vertice
        :param destination: destination vertice
        :return: shortest distance between #origin and #destination
        """

        distance = list()
        queue = list()
        vertice_index_helper = dict()  # aux
        index_vertice_helper = dict()  # aux
        removed_from_queue = []  # aux

        # Sets the initial distance values for each vertice in the graph
        # Distance from origin to vertice is 0 iff vertice == origin and origin != destination
        for index, vertice in enumerate(self.vertices):
            if vertice == origin and origin != destination:
                distance.append(0)
            else:
                distance.append(INF)

            queue.append(vertice)
            vertice_index_helper[vertice] = index
            index_vertice_helper[index] = vertice

        if origin == destination:
            # fill all distance between source and its adjacent vertices
            for v in self.vertices[origin]:
                distance[vertice_index_helper[v]] = self.vertices[origin][v]

        # While queue is not empty
        while len(queue) > 0:
            # Remove vertice with minimum distance from origin
            min_index = find_min_index(distance, removed_from_queue)
            removed_from_queue.append(min_index)
            u = index_vertice_helper[min_index]

            index = queue.index(u)
            del queue[index]

            distance_to_u = distance[vertice_index_helper[u]]

            # For each vertice adjancet to u
            for v in self.vertices[u]:

                v_index = vertice_index_helper[v]

                distance_to_v = distance[v_index]

                # Relaxation step
                if distance_to_v > distance_to_u + self.vertices[u][v]:
                    distance[v_index] = distance_to_u + self.vertices[u][v]

        return distance[vertice_index_helper[destination]]
