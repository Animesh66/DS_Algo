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


graph = DirectGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('D', 'A')
graph.add_edge('B', 'C')
# graph.remove_edge('A', 'B')
graph.remove_vertex('A')
graph.print_graph()
