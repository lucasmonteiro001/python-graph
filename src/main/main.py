"""Main module. Runs the tests given in the documentation"""

from src.main.graph import Graph
from src.util import PrintUtil, InputUtil, ParserUtil

LINE = InputUtil.read_standard_input()

EDGES = ParserUtil.parse_string(LINE)

# Instantiates a new graph
graph = Graph()

# Add the EDGES to the graph
for e in EDGES:
    graph.add_edge(e.origin, e.destination, e.distance)

# Test #1
PrintUtil.print_string_to_standard_output(
    graph.find_route_distance_among_vertices(["A", "B", "C"]))

# Test #2
PrintUtil.print_string_to_standard_output(
    graph.find_route_distance_among_vertices(["A", "D"]))

# Test #3
PrintUtil.print_string_to_standard_output(
    graph.find_route_distance_among_vertices(["A", "D", "C"]))

# Test #4
PrintUtil.print_string_to_standard_output(
    graph.find_route_distance_among_vertices(["A", "E", "B", "C", "D"]))

# Test #5
PrintUtil.print_string_to_standard_output(
    graph.find_route_distance_among_vertices(["A", "E", "D"]))

# Test #6
PrintUtil.print_string_to_standard_output(
    graph.get_total_trips_max_stops("C", "C", 3))

# Test #7
PrintUtil.print_string_to_standard_output(
    graph.get_total_trips_exact_stops("A", "C", 4))

# Test #8
PrintUtil.print_string_to_standard_output(
    graph.get_shortest_distance("A", "C"))

# Test #9
PrintUtil.print_string_to_standard_output(
    graph.get_shortest_distance("B", "B"))

# Test #10
PrintUtil.print_string_to_standard_output(
    graph.get_total_trips_distance_less_than("C", "C", 30))
