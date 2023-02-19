from Graph.AdjacencyListGraph import AdjacencyListGraph
from Graph.AdjacencyMatrixGraph import AdjacencyMatrixGraph
from Graph.EdgeListGraph import EdgeListGraph
from Graph.GraphHelper import GraphHelper
from Graph.Vertex import Vertex


def dive_into_space():
    # (Radius in km, gravity in m/s2)
    # draw the graph on paper to better visualize connections
    earth = Vertex('earth', (6371, 9.807))
    sun = Vertex('sun', (696340, 274))
    jupiter = Vertex('jupiter', (69911, 24.79))
    saturn = Vertex('saturn', (58232, 10.44))
    uranus = Vertex('uranus', (25362, 8.87))
    pluto = Vertex('pluto', (1188.3, 0.62))

    # create graph from starting vertices
    solar_system = [earth, sun, jupiter, saturn, uranus, pluto]
    # milky_way = EdgeListGraph(solar_system)
    # milky_way = AdjacencyMatrixGraph(solar_system, directed=False)
    milky_way = AdjacencyListGraph(solar_system, directed=True)

    # add vertex from provided label and data
    milky_way.add_vertex('venus', (6051.8, 8.87))
    milky_way.add_vertex('neptune', (24622, 11.15))

    # distance in light years
    milky_way.add_edge('sun', 'earth', 1.581E-05)
    milky_way.add_edge('sun', 'venus', 1.1362E-05)
    milky_way.add_edge('earth', 'venus', 4.4E-06)
    milky_way.add_edge('earth', 'jupiter', 8.271665726E-9)
    milky_way.add_edge('jupiter', 'saturn', 683108E-4)
    milky_way.add_edge('saturn', 'neptune', 3251757E-3)
    milky_way.add_edge('jupiter', 'uranus', 2214649E-3)
    milky_way.add_edge('neptune', 'pluto', 4.75E-3)

    print(milky_way)

    start_vertex = 'earth'
    connected_planets = milky_way.find_connected_vertices(milky_way.find_vertex(start_vertex))
    print(f'\nConnected planets to {start_vertex} are : {connected_planets}')

    start_vertex = 'saturn'
    milky_way.directed = True
    walk = milky_way.bf_walk(milky_way.find_vertex(start_vertex))
    print(f'\nWalking down iteratively an directed graph levelwise starting from vertex: {start_vertex}')
    for v in walk:
        print(v)

    start_vertex = 'saturn'
    milky_way.directed = False
    iterative_walk = milky_way.bf_walk(milky_way.find_vertex(start_vertex))
    print(f'\nWalking down iteratively the non-directed graph levelwise starting from vertex: {start_vertex}')
    for v in iterative_walk:
        print(v)

    start_vertex = 'earth'
    milky_way.directed = True
    iterative_walk = milky_way.df_walk(milky_way.find_vertex(start_vertex))
    recursive_walk = milky_way.df_walk_recursive(milky_way.find_vertex(start_vertex))
    print(f'\nWalking down iteratively the galaxy depth-first starting from vertex: {start_vertex}')
    for v in iterative_walk:
        print(v)
    print(f'\nWalking down recursively the galaxy depth-first starting from vertex: {start_vertex}')
    for v in recursive_walk:
        print(v)

    print('\nFind strongly connected components for a graph:')
    milky_way.directed = False
    connected_components = GraphHelper.find_connected_components(milky_way)
    for cc in connected_components.keys():
        print(f'Starting vertex: {str(cc)} -> Connected Component is: {connected_components[cc]}')

    print('\nFind sinks')
    sinks = GraphHelper.find_sinks(milky_way)
    print(sinks)

    print('\nall ok.')


dive_into_space()
