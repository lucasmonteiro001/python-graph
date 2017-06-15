class Edge(object):
    def __init__(self, origin, destination, distance):
        super(Edge, self).__init__()
        self.origin = origin
        self.destination = destination
        self.distance = float(distance)

    def __str__(self):
        return 'from:{}, to:{}, distance:{}'.format(self.origin, self.destination, self.distance)