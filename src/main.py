from src import PrintUtil, InputUtil, ParserUtil

from graph import Graph

line = InputUtil.read_standard_input()

edges = ParserUtil.parse_string(line)

# Instantiates a new graph
graph = Graph()

# Add the edges to the graph
for e in edges:
    graph.add_edge(e.origin, e.destination, e.distance)

# Test #1
PrintUtil.print_string_to_standard_output(graph.find_route_distance_among(["A", "B", "C"]))

# Test #2
PrintUtil.print_string_to_standard_output(graph.find_route_distance_among(["A", "D"]))

# Test #3
PrintUtil.print_string_to_standard_output(graph.find_route_distance_among(["A", "D", "C"]))

# Test #4
PrintUtil.print_string_to_standard_output(graph.find_route_distance_among(["A", "E", "B", "C", "D"]))

# Test #5
PrintUtil.print_string_to_standard_output(graph.find_route_distance_among(["A", "E", "D"]))

# Test #6
PrintUtil.print_string_to_standard_output(graph.number_of_trips_starting_at_ending_at_max_stops("C", "C", 3))

# Test #7
PrintUtil.print_string_to_standard_output(graph.number_of_trips_starting_at_ending_at_exactly_stops("A", "C", 4))

# Test #8
PrintUtil.print_string_to_standard_output(graph.shortest_distance("A", "C"))

# Test #9
PrintUtil.print_string_to_standard_output(graph.shortest_distance("B", "B"))

# Test #10
PrintUtil.print_string_to_standard_output(graph.number_of_trips_starting_at_ending_at_distance_less_than("C", "C", 30))
