
# """
# Simple graph implementation
# """

# import os
# from util import Stack, Queue  # These may come in handy
# os.system( 'clear' )

# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):

#         self.vertices = {}
#         self.storage = set()

#     def add_vertex(self, vertex):

#         """
#         Add a vertex to the graph.
#         """

#         self.vertices[vertex] = set()

#     def add_edge(self, v1, v2):

#         """
#         Add a directed edge to the graph.
#         """

#         if v1 in self.vertices and v2 in self.vertices:

#             self.vertices[v1].add(v2)

#         else:

#             raise IndexError("That vertex does not exist.")

#     def bft(self, starting_vertex):

#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """

#         # Create an empty queue and enqueue the starting vertex ID
#         q = Queue()
#         q.enqueue(starting_vertex)

#         # Create an empty Set to store visited vertices
#         visited = set()

#         # While the queue is not empty...
#         while q.size() > 0:

#             # Dequeue the first vertex
#             v = q.dequeue()

#             # If that vertex has not been visited...
#             if v not in visited:

#                 # Mark it as visited
#                 print(v)
#                 visited.add(v)

#                 # Then add all of its neighbors to the back of the queue
#                 for neighbor in self.vertices[v]:
#                     q.enqueue(neighbor)

#     def dft(self, starting_vertex):

#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """

#         # Create an empty stack and push the starting vertex ID
#         s = Stack()
#         s.push(starting_vertex)

#         # Create a Set to store visited vertices
#         visited = set()

#         # While the stack is not empty...
#         while s.size() > 0:

#             # Pop the first vertex
#             v = s.pop()

#             # If that vertex has not been visited...
#             if v not in visited:

#                 # Mark it as visited...
#                 print(v)
#                 visited.add(v)

#                 # Then add all of its neighbors to the top of the stack
#                 for neighbor in self.vertices[v]:
#                     s.push(neighbor)

#     # Todo
#     print( '\nRecursive Depth First Traversal\n' )
#     def dft_recursive(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         This should be done using recursion.
#         """

#         print( starting_vertex  )

#         selected = self.vertices[ starting_vertex ]

#         # print( 'STORAGE:' , self.storage )
#         q = Queue()

#         if starting_vertex not in self.storage:
#             self.storage.add( starting_vertex )

#         if len( selected ) >= 2:

#             # print( 'Alternate paths:' )
#             q.enqueue( starting_vertex )
#             for i in selected:
#                 self.dft_recursive( i )

#         # else:

#         for x in selected:

#             if x not in self.storage:
#                 self.storage.add( x )
#                 self.dft_recursive( x )

#         print( '\n' )

#         if len( q.queue ) is not 0:

#             ind = q.queue[0]

#             print( ind )

#     # Todo
#     def bfs(self, starting_vertex, destination_vertex):
    
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
        
#         print( 'Bredth First Search' )
#         # Create an empty queue and enqueue A PATH TO the starting vertex ID
#         q = Queue()
#         q.enqueue( starting_vertex )

#         print( starting_vertex )

#         # Create a Set to store visited vertices
#         visited = set()
#         path = []
#         path.append( starting_vertex )

#         # While the queue is not empty...
#         while q.queue:

#             # Dequeue the first PATH
#             temp = self.vertices[ q.queue[0] ]
#             print( 'temp' , temp )
#             the_queue = []

#             # Grab the last vertex from the PATH
#             if len( temp ) >= 2:
#                 for i in temp:
#                     print( i )
#                     the_queue.insert( 0 , i )

#             if len( the_queue ) >= 2:
#                 temp = the_queue
#                 print( 'New Temp:' , temp )

#             for i in temp:
#                 path.append( i )

#                 # CHECK IF IT'S THE TARGET
#                 if i == destination_vertex:
#                     path.append( i )
#                     print( visited )
#                     # IF SO, RETURN PATH
#                     return path

#                 # If that vertex has not been visited...
#                 if i in visited:
#                     None

#                 for x in self.vertices[ i ]:
#                     if x == destination_vertex:
#                         path.append( x )
#                         return path
                        
#                 print( i )
#                 q.enqueue(i)

#                 # Mark it as visited...
#                 visited.add( q.queue[0] )
#                 q.queue.pop(0)
#                 print( visited )
#                 break


#                 # Then add A PATH TO its neighbors to the back of the queue
#                   # COPY THE PATH
#                   # APPEND THE NEIGHOR TO THE BACK

#     # Todo
#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         print( 'Depth First Search' )

#         q = Queue()
#         q.enqueue( starting_vertex )

#         print( starting_vertex )

#         visited = set()
        
#         path = [[],[]]
#         path[0].append( starting_vertex )
#         path[1].append( starting_vertex )

#         while q.queue:

#             temp = self.vertices[ q.queue[0] ]
#             print( 'temp' , temp )
#             the_queue = []

#             if len( temp ) >= 2:
#                 for i in temp:
#                     print( i )
#                     the_queue.insert( 0 , i )
#                 temp = the_queue
#                 print( 'New Temp:' , temp )

#             for i in temp:

#                 print( 'PATH' , path )
#                 path[0].append( i )
#                 path[1].append( i )
#                 q.enqueue(i)

                    
#                 for x in self.vertices[ i ]:

#                     if x == destination_vertex:
                        
#                         for i in self.vertices[ path[0][len( path[0] ) - 1] ]:
#                             if i == destination_vertex:
#                                 path[1].append( x )
#                             else:
#                                 path[0].append( i )
#                                 for i in self.vertices[ path[0][len( path[0] ) - 1] ]:
#                                     if i == destination_vertex:
#                                         path[0].append( i )

#                         return path
                            
#                 print( i )
#                 q.queue.pop(0)
#                 break



# LECTURE NOTES

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Initialize visited, if it hasn't bee initialized yet
        if visited is None:
            visited = set()
        print(f'Starting vertex: {starting_vertex}')
        # If the vertex has not been visited...
        if starting_vertex not in visited:            
            # Mark the node as visited
            print(starting_vertex) 
            visited.add(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:

            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:

                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:

                    # IF SO, RETURN PATH
                    return path    

                # Mark it as visited...
                visited.add(v)

                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):

                    # COPY THE PATH
                    # path_copy = list(path)
                    path_copy = path.copy()
                    
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path              
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                  # COPY THE PATH
                #   path_copy = list(path)
                  path_copy = path.copy()
                  # APPEND THE NEIGHOR TO THE BACK
                  path_copy.append(neighbor)
                  s.push(path_copy)
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
