"""This module contains the class that represents the edges of the graph"""


class Edge(object):
    """This class represents the edge of a graph"""

    def __init__(self, origin, destination, distance):
        """
        Constructor
        :param origin: id of origin vertice
        :param destination: id of destination vertice
        :param distance: distance between origin and destination
        """
        self.origin = origin
        self.destination = destination
        self.distance = int(distance)

    def __str__(self):
        return 'from:{}, to:{}, distance:{}'.format(self.origin, self.destination, self.distance)
