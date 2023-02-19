
class GraphHelper(object):

    @classmethod
    def find_connected_components(cls, graph) -> {}:
        # dictionary of connected components
        # key = starting vertex
        # value = corresponding strongly connected components
        connected_components = {}
        vertices = graph.graph_dict.keys()
        while len(vertices) > 0:
            start_vertex = next(iter(vertices))
            components = graph.bf_walk(start_vertex)
            connected_components[start_vertex] = components
            diff = lambda l1, l2: [x for x in l1 if x not in l2]
            vertices = diff(vertices, components)
            # vertices = list(set(vertices) - set(components))
        return connected_components

    # Check if all non-zero degree vertices are connected
    def is_eulerian(self, graph):
        pass

    def is_euclidean(self, graph):
        pass

    # if all the vertices are visited, then hamiltonian path exists
    def is_hamiltonian(self, graph):
        pass

    # input : acyclic digraph of n nodes and m edges
    # output: list of sink nodes
    # A sink node is a node such that no edge emerges out of it.
    @classmethod
    def find_sinks(cls, graph) -> []:
        working_dict = {vertex: True for vertex in graph.vertices()}
        edges = graph.edges()
        for edge in edges:
            working_dict[edge.origin] = False
        sinks = []
        for vertex in working_dict.keys():
            if working_dict.get(vertex) is True:
                sinks.append(vertex)
        return sinks



