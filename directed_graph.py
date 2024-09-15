class _Node:

    def __init__(self, label: str) -> None:
        self.label = label


class DirectGraph(_Node):
    """
    This is a graph class represented with adjacency list format.
    Graph can be implemented using either adjacency list format 
    or using adjacency matrix format.
    """

    def __init__(self) -> None:
        """
        The contructor will create the adjacency list dict
        """
        self.adj_list = {}

    def print_graph(self) -> None:
        """
        This helper method will print a graph like below 
        where keys in the dict are vertex and values in the list are 
        edges connected with vertex.
                            A
                           /  \
                          B -- C
        The above graph will be printed as below.
        {
            'A' : ['B', 'C'],
            'B' : ['A', 'C'],
            'C' : ['A', 'B']
        }
        """
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} : {edges}")

    def add_vertex(self, vertex: str) -> bool:
        """
        Method to add new vertex to a graph.
        """
        # if there are no vertex present then add the vertex in the adjacency list dictionary
        """
        This will create a graph like this
        {
            'A': []
        }
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def __verify_vertices_exists(self, vertices: list[str]) -> bool:
        """
        This method will verify if the given vertices exists or not.
        If any vertex did not exists then this method will return False. Else return true.
        """
        for vertex in vertices:
            if vertex not in self.adj_list.keys():
                return False
        return True

    def add_edge(self, first_vertex: str, second_vertex: str) -> bool:
        """
        This method will connect two vertex with an edge.
        """
        # before creating an edge ensure that both of the vertex did exists else return false
        # This is a uni-direct graph not a non-directed graph.
        if self.__verify_vertices_exists(vertices=[first_vertex, second_vertex]):
            self.adj_list[first_vertex].append(second_vertex)
            return True
        return False

    def remove_edge(self, first_vertex: int, second_vertex: int) -> bool:
        """
        This method will remove an edge between two vertices.
        """
        # we need to use the try block here in case the given
        # two vertices does not connect with an edges.

        if self.__verify_vertices_exists(vertices=[first_vertex, second_vertex]):
            try:
                self.adj_list[first_vertex].remove(second_vertex)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, selected_vertex: str) -> bool:
        """
        This method will remove the given vertex.
        """
        # if vertex exists then first loop over the edges present for the vertex and remove them
        # after that delete the vertex from the dict.
        if self.__verify_vertices_exists(vertices=[selected_vertex]):
            for vertex in self.adj_list.keys():
                if selected_vertex in self.adj_list[vertex]:
                    self.adj_list[vertex].remove(selected_vertex)
            del self.adj_list[selected_vertex]
            return True
        return False

    def dfs_traversal_directed_graph(self, vertex: str) -> None:
        """
        This helper method will provide the depth first travesal path of a directed graph.
        """
        # check if the vertex provided exists or nots
        if not self.__verify_vertices_exists([vertex]):
            return
        # if vertex exists then call the private recursive method with values.
        # here vertex is the provided vertex and set is a blank set.
        self.__dfs_traversal_directed_graph(
            vertex=vertex, visited_vertices=set())

    def __dfs_traversal_directed_graph(self, vertex: str, visited_vertices: set) -> None:
        """
        This private method will provide the depth first travesal path of a directed graph.
        """
        # first print the provided vertex and then add this to the set.
        print(vertex)
        visited_vertices.add(vertex)
        for v in self.adj_list.get(vertex):
            if v not in visited_vertices:
                self.__dfs_traversal_directed_graph(v, visited_vertices)

    def dfs_traverse_non_recursive(self, vertex: str) -> None:
        """
        This method will print the vertx in depth first travesal.
        """
        # first verify that vertex is a valid vertex.
        if not self.__verify_vertices_exists([vertex]):
            return
        # create an empty set to track the list of vistex vertex.
        # create an empty list and push the vertex in the list
        visited_vertex = set()
        stack = []
        stack.append(vertex)
        #  while the list is not empty
        while len(stack) > 0:
            #  set the current element to the top of the stack
            current = stack.pop()
            # verify if the currect vertex is in visited vertex set the start the
            # loop again
            if current in visited_vertex:
                continue
            # if the vertex is not visited then print the vertex and add it to the set of visited vertex.
            print(current)
            visited_vertex.add(current)
            # visit the neighbour vertices using a for loop
            for neighbour in self.adj_list.get(current):
                if neighbour not in visited_vertex:
                    stack.append(neighbour)


graph = DirectGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('B', 'D')
graph.add_edge('D', 'C')
graph.add_edge('A', 'C')
# graph.remove_edge('A', 'B')
# graph.remove_vertex('A')
# graph.print_graph()
# graph.dfs_traversal_directed_graph('G')
graph.dfs_traverse_non_recursive('A')
