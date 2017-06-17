import unittest
from tests import Graph

NO_SUCH_ROUTE = "NO SUCH ROUTE"


def create_graph_test():
    graph = Graph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "C", 4)
    graph.add_edge("C", "D", 8)
    graph.add_edge("D", "C", 8)
    graph.add_edge("D", "E", 6)
    graph.add_edge("A", "D", 5)
    graph.add_edge("C", "E", 2)
    graph.add_edge("E", "B", 3)
    graph.add_edge("A", "E", 7)

    return graph


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graphTest = create_graph_test()

    def test_constructor(self):
        self.assertIsNotNone(self.graph.vertices)

    def test_add_edges(self):
        graph = self.graph

        graph.add_edge("a", "b", 1)
        graph.add_edge("a", "s", 1)
        graph.add_edge("b", "s", 1)

        self.assertEquals(len(self.graph.vertices), 2, "Two items were added to the vertices list")
        self.assertEquals(len(self.graph.vertices["a"]), 2, "Vertice 'a' has only 2 adjacent vertices")
        self.assertEquals(len(self.graph.vertices["b"]), 1, "Vertice 'b' has only 1 adjacent vertice")

    def test_1(self):
        self.assertEquals(self.graphTest.find_route_distance_among_vertices(["A", "B", "C"]), 9)

    def test_2(self):
        self.assertEquals(self.graphTest.find_route_distance_among_vertices(["A", "D"]), 5)

    def test_3(self):
        self.assertEquals(self.graphTest.find_route_distance_among_vertices(["A", "D", "C"]), 13)

    def test_4(self):
        self.assertEquals(self.graphTest.find_route_distance_among_vertices(["A", "E", "B", "C", "D"]), 22)

    def test_5(self):
        self.assertEquals(self.graphTest.find_route_distance_among_vertices(["A", "E", "D"]), NO_SUCH_ROUTE)

    def test_6(self):
        self.assertEquals(self.graphTest.get_total_trips_between_origin_destination_max_stops("C", "C", 3), 2)

    def test_7(self):
        self.assertEquals(self.graphTest.get_total_trips_between_origin_destination_exactly_stops("A", "C", 4), 3)

    def test_8(self):
        self.assertEquals(self.graphTest.get_shortest_distance("A", "C"), 9)

    def test_9(self):
        self.assertEquals(self.graphTest.get_shortest_distance("B", "B"), 9)

    def test_10(self):
        self.assertEquals(self.graphTest.get_total_trips_between_origin_destination_distance_less_than("C", "C", 30), 7)
