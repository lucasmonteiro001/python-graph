import unittest
from src.edge import Edge


class ParserTestCase(unittest.TestCase):
    def test_constructor(self):
        origin = "A"
        destination = "B"
        distance = 7

        edge = Edge(origin, destination, distance)

        self.assertTrue(edge.origin == origin and edge.destination == destination and edge.distance == distance)

    def test_invalid_argument(self):
        origin = "A"
        destination = "B"
        distance = "7a"

        with self.assertRaises(ValueError):
            Edge(origin, destination, distance)
