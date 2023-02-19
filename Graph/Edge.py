
class Edge(object):
    def __init__(self, source_vertex, destination_vertex, data):
        self.origin = source_vertex
        self.destination = destination_vertex
        self.data = data

    def hash(self):
        return hash((self.destination, self.destination))

    def __str__(self):
        return f'\n({str(self.origin)},{str(self.destination)},{str(self.data)})'

    def __repr__(self):
        return self.__str__()
