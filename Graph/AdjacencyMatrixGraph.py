from Graph.Edge import Edge
from Graph.Vertex import Vertex


class AdjacencyMatrixGraph(object):

    # Graph = (V, E)
    def __init__(self, vertices=[], edges=[], directed=True, max_size=10):
        self.vertices = dict()
        self.size = 0
        self.max_size = max_size
        for vertex in vertices:
            self.vertices[vertex.key] = (vertex, self.size)
            self.size += 1
        self.matrix = [[None] * self.max_size for _ in range(self.max_size)]
        self.directed = directed

    def find_index(self, vertex_key):
        if vertex_key in self.vertices:
            return self.vertices[vertex_key][1]
        else:
            return -1

    def find_vertex(self, vertex_key):
        if vertex_key in self.vertices:
            return self.vertices[vertex_key][0]
        else:
            return None

    def get_vertex(self, vertex_index):
        for vertex in self.vertices.values():
            if vertex[1] == vertex_index:
                return vertex
        return None

    def add_vertex(self, key, data):
        new_vertex = Vertex(key, data)
        self.vertices[key] = (new_vertex, self.size)
        self.size += 1

    def add_edge(self, source_key, destination_key, data):
        u = self.find_index(source_key)
        v = self.find_index(destination_key)
        self.matrix[u][v] = data
        # if self.directed:
        #    self.matrix[v][u] = data

    # Return a set of all edges of the graph
    def edges(self):
        to_return = set()
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] is not None:
                    vertex_from = self.get_vertex(i)
                    vertex_to = self.get_vertex(j)
                    new_edge = Edge(vertex_from, vertex_to, self.matrix[i][j])
                    to_return.add(new_edge)
        return to_return

    # levelwise traversal of the graph
    def bf_walk(self, start_vertex):
        return []

    def __str__(self):
        return ''.join(map(str, self.edges()))

    def __repr__(self):
        return self.__str__()
