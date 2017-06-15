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


# graph.number_of_trips_starting_at_ending_at_max_stops("C", "C", 3)
graph.number_of_trips_starting_at_ending_at_exactly_stops("A", "C", 4)

exit()

# 1
print graph.find_route_distance_among(["A", "B", "C"])
# 2
print graph.find_route_distance_among(["A", "D"])
# 3
print graph.find_route_distance_among(["A", "D", "C"])
# 4
print graph.find_route_distance_among(["A", "E", "B", "C", "D"])
# 5
print graph.find_route_distance_among(["A", "E", "D"])
