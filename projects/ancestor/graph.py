"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        If both exist, and a connection from v1 to v2
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        Pseudo - Create Stack/Queue, Put starting point
        While there is stuff in data structure, 
        Pop first item

        """
        # TODO
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            vertex = stack.pop()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

# Following function will allow us determine path to oldest ancestor
# Modified version of DFS
    def earliest(self, starting_vertex):
        stack = Stack()
        # Put the starting point in that
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # Track the path
        longest_path = [starting_vertex]
        # While there is stuff in the queue/stack
        while stack.size() > 0:

            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                visited.add(vertex)
        # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy the path
                    new_path = list(path)
                    new_path.append(next_vert)
                    # Add that edge to the queue/stack
                    stack.push(new_path)
                    # compare the path lengths and update
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
                    # path may be same size size but path has changed so check last element for change
                    if len(new_path) == len(longest_path) and new_path[-1] != longest_path[-1]:
                        longest_path = new_path
        return longest_path
