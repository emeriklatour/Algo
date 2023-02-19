from Graph.Edge import Edge
from Graph.Vertex import Vertex


class AdjacencyListGraph(object):

    def __init__(self, vertices=[], directed=True):
        # hashtable that maps vertex to a list of edges
        # key is vertex, value is connected edges
        # dict.fromkeys(vertices, None)
        self.graph_dict = {key: [] for key in vertices}
        self.directed = directed

    # Return an iteration of all vertices of the graph
    def vertices(self):
        return self.graph_dict.keys()

    # Return the number of edges in the graph
    def edge_count(self):
        total = sum(len(self.graph_dict[v]) for v in self.graph_dict)
        return total

    # Return a set of all edges of the graph
    def edges(self):
        to_return = set()
        for v in self.graph_dict:
            to_return.update(self.graph_dict.get(v))
        return to_return

    def find_vertex(self, key):
        for vertex in self.graph_dict.keys():
            if vertex.key == key:
                return vertex
        return None

    def add_vertex(self, key, data):
        new_vertex = Vertex(key, data)
        self.graph_dict[new_vertex] = []

    def add_edge(self, origin_key, destination_key, data=None):
        origin_vertex = self.find_vertex(origin_key)
        destination_vertex = self.find_vertex(destination_key)
        new_edge = Edge(origin_vertex, destination_vertex, data)
        self.graph_dict[origin_vertex].append(new_edge)

    def find_connected_vertices(self, start_vertex):
        connected = []
        outgoing_edges = self.graph_dict[start_vertex]
        for edge in outgoing_edges:
            connected.append(edge.destination)
        if not self.directed:
            for vertex in self.graph_dict.keys():
                outgoing_edges = self.graph_dict[vertex]
                for edge in outgoing_edges:
                    if edge.destination == start_vertex:
                        connected.append(vertex)
        return connected

    # levelwise traversal of a graph
    # iterative version
    def bf_walk(self, start_vertex):
        levelwise_walk = []
        to_visit_queue = [start_vertex]
        while len(to_visit_queue) > 0:
            current_vertex = to_visit_queue.pop(0)
            connected_vertices = self.find_connected_vertices(current_vertex)
            for vertex in connected_vertices:
                if vertex not in levelwise_walk and vertex not in to_visit_queue:
                    to_visit_queue.append(vertex)
            if current_vertex not in levelwise_walk:
                levelwise_walk.append(current_vertex)
        return levelwise_walk

    # depth-first traversal of a graph
    # iterative version
    def df_walk(self, start_vertex):
        depth_first_walk = []
        to_visit_stack = [start_vertex]
        while len(to_visit_stack) > 0:
            current_vertex = to_visit_stack.pop()
            connected_vertices = self.find_connected_vertices(current_vertex)
            for vertex in connected_vertices:
                if vertex not in depth_first_walk and vertex not in to_visit_stack:
                    to_visit_stack.append(vertex)
            if current_vertex not in depth_first_walk:
                depth_first_walk.append(current_vertex)
        return depth_first_walk

    # depth-first traversal of a graph
    # recursive version
    def df_walk_recursive(self, start_vertex):
        return self.go_df(start_vertex, [])

    def go_df(self, start_vertex, visited):
        visited.append(start_vertex)
        for neighbor in self.find_connected_vertices(start_vertex):
            if neighbor not in visited:
                visited = self.go_df(neighbor, visited)
        return visited

    def __str__(self):
        return ''.join(map(str, self.edges()))

    def __repr__(self):
        return self.__str__()
