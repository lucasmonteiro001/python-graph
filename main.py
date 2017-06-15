from sys import stdin
from collections import defaultdict


class InputUtil(object):
    @staticmethod
    def read_standard_input():
        try:
            input = stdin.readline()
            return input
        except Exception:
            raise Exception("Error reading standard input")


class Vertice(object):
    def __init__(self):
        super(Vertice, self).__init__()


class Edge(object):
    def __init__(self, origin, destination, distance):
        super(Edge, self).__init__()
        self.origin = origin
        self.destination = destination
        self.distance = float(distance)

    def __str__(self):
        return 'from:{}, to:{}, distance:{}'.format(self.origin, self.destination, self.distance)


class ParserUtil(object):
    @staticmethod
    def __parse(element):
        return Edge(element[0], element[1], element[2:])

    @staticmethod
    def parse_line(line):
        # Token responsible for the parse
        token = ","

        # remove trailing/leading/repeated spaces before parsing
        return map(ParserUtil.__parse, " ".join(line.split(token)).split())


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, origin, destination, weight):
        self.graph[origin].append([destination, weight])


# line = InputUtil.read_standard_input()

# print line
edges = ParserUtil.parse_line("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")

graph = Graph()

for e in edges:
    graph.add_edge(e.origin, e.destination, e.distance)

print graph
