from InputUtil import InputUtil
from ParserUtil import ParserUtil
from Graph import Graph

# line = InputUtil.read_standard_input()

# print line
# edges = ParserUtil.parse_line(line)
edges = ParserUtil.parse_line("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")

# Instantiates a new graph
graph = Graph()

# Add the edges to the graph
for e in edges:
    graph.add_edge(e.origin, e.destination, e.distance)


print graph.vertices["A"]
