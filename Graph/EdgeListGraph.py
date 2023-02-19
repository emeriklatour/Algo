from Graph.Edge import Edge
from Graph.Vertex import Vertex


class EdgeListGraph(object):

    # Graph = (V, E)
    def __init__(self, vertices=[], edges=[],
                 directed=True):
        # vertices are mandatory for a
        # non-connected vertex
        self.vertices = vertices
        self.edges = edges
        self.directed = directed

    def add_vertex(self, key, data):
        new_vertex = Vertex(key, data)
        self.vertices.append(new_vertex)

    def add_edge(self, new_edge):
        if new_edge is not None:
            self.edges.append(new_edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def add_edge(self, origin_key, destination_key, data):
        origin_vertex = self.find_vertex(origin_key)
        destination_vertex = self.find_vertex(destination_key)
        new_edge = Edge(origin_vertex, destination_vertex, data)
        self.edges.append(new_edge)

    def find_vertex(self, key):
        for vertex in self.vertices:
            if vertex.key == key:
                return vertex
        return None

    def __str__(self):
        return ''.join(map(str, self.edges))

    def __repr__(self):
        return self.__str__()
