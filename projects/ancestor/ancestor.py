from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Initialize the graph
    ancestor_graph = Graph()
    # We need store ancestry tree. Testing with data provided
    # List is provided, which contains, each element is a set of two elements
    # Let add vertices which involve of a parent and a child from each set inside of list

    # Loop through ancestor and add each set as vertices
    for each_group in ancestors:
        # Add first vertex and then second one
        ancestor_graph.add_vertex(each_group[0])
        ancestor_graph.add_vertex(each_group[1])

    # All vertices are added and needs to connected appropriately
    # Lets add the edges
    # edges inside of Graph are directed
    # So the edge must go grom a child in position [1] to parent in position [0]
    # Depth first search will allow us to find longest chain
    # Also if vertex doesn't have a parent returns -1
    for each_group in ancestors:
        ancestor_graph.add_edge(each_group[1], each_group[0])

    ancestor = ancestor_graph.dft(starting_node)


list_of_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                     (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(list_of_ancestors, 3)
