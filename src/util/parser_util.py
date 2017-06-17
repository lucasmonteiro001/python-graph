"""Module responsible for parsing utilities"""

from src.main.edge import Edge


class ParserUtil(object):
    """Class that contains functions to parse a line into a list of edges"""

    @staticmethod
    def __parse(element):
        """
        Parses an #element
        :param element: element to be parsed
        :return: returns an edge with the data parsed from the #element
        """
        return Edge(element[0], element[1], element[2:])

    @staticmethod
    def parse_string(string):
        """
        Given a #line, return a list of edges
        :param string: line to be parsed
        :return: returns a list of edges
        """

        # Token delimiter
        token = ","

        try:
            # remove trailing/leading/repeated spaces before parsing
            return map(ParserUtil.__parse, " ".join(string.split(token)).split())
        except Exception:
            raise ValueError("Invalid input."
                             "\nEach edge should be separeted by comma."
                             "\nEach edge is composed of: two letters and one positive integer"
                             "\nExample: AX9, FW12, KB72")
