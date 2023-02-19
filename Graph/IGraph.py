

class IGraph(object):

    # Assuming vertex v is one endpoint of the edge
    # (either origin or destination), return the other endpoint.
    def _connections(self, vertex):
        pass

    # Return the number of vertices of the graph.
    def _vertex_count(self):
        pass

    # Return the number of edges of the graph.
    def _edge_count(self):
        pass

    # Return an iteration of all the vertices of the graph.
    def _vertices(self):
        pass

    # Return an iteration of all the edges of the graph.
    def _edges(self):
        pass

    # Return the edge from vertex u to vertex v, if one exists;
    # otherwise return None. For an undirected graph, there is
    # no difference between get edge(u,v) and get edge(v,u).
    def _get_edge(self, u, v):
        pass

    # For an undirected graph, return the number of edges incident
    # to vertex v. For a directed graph, return the number
    # of outgoing (resp. incoming) edges incident to vertex v,
    # as designated by the optional parameter.
    def _degree(self, v):
        pass

    # Create and return a new Vertex storing element data.
    def _add_vertex(self, key, data=None):
        pass

    # Create and return a new Edge from vertex u to vertex v,
    # storing element data (None by default).
    def _add_edge(self, u, v, data=None):
        pass

    # Remove vertex v and all its incident edges from the graph.
    def _remove_vertex(self, key):
        pass

    # Remove edge e from the graph.
    def _remove_edge(self, e):
        pass

    def is_directed(self):
        pass


