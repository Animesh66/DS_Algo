class DirectedGraph:
    """
    This is a graph class represented with adjacency list format.
    Graph can be implemented using either adjacency list format 
    or using adjacency matrix format.
    """
    class _Node:

        def __init__(self, label: str) -> None:
            self.label = label

    class _Edge:

        def __init__(self, from_node: str, to_node: str, weight: int) -> None:
            self.from_node = from_node
            self.to_node = to_node
            self.weigh = weight

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
                          1 /  \ 2
                           B --  C
                              2
        The above graph will be printed as below.
        {
            'A' : [{'B': 1}, {'C': 2}],
            'B' : [{'A': 1}, {'C': 2}],
            'C' : [{'A': 2}, {'B': 2}]
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

    def add_edge(self, first_vertex: str, second_vertex: str, weight: int) -> bool:
        """
        This method will connect two vertex with an edge.
        """
        # before creating an edge ensure that both of the vertex did exists else return false
        # This is a uni-direct graph not a non-directed graph.
        if self.__verify_vertices_exists(vertices=[first_vertex, second_vertex]):
            self.adj_list[first_vertex].append({second_vertex: weight})
            self.adj_list[second_vertex].append({first_vertex: weight})
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
                for edges in self.adj_list[first_vertex]:
                    if second_vertex in edges:
                        del edges
                for edges in self.adj_list[second_vertex]:
                    if first_vertex in edges:
                        del edges
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
            for vertex in self.adj_list[selected_vertex]:
                self.adj_list[vertex].remove(selected_vertex)
            del self.adj_list[selected_vertex]
            return True
        return False

    def has_cycle(self) -> bool:
        """
        This method will return true if the this undirected graph has cycle.
        Mehod will return true if the graph has cycle otherwise return false.
        """
        #  Create a set of all visisted vertex
        visited_vertex = set()
        # iteratively visit all vertex and do a breath first search for all the vertex
        # and find if the vertex is in visted set or not
        for vertex in self.adj_list.keys():
            if vertex not in visited_vertex and self.__has_cycle(vertex, None, visited_vertex):
                return True
        return False

    def __has_cycle(self, vertex: str, parent_vertex: str | None, visited_vertex: set[str]) -> bool:
        """
        Private recursive method for doing a breadth first seach algorithm.
        """
        #  First put the current vertex to the visisted set.
        visited_vertex.add(vertex)
        # Visit all the vertex iteratively and skip the parent vertex and recursively visit all the vertex.

    def depth_first_search_direct_graph(self, vertex: str):
        """
        This is a depth first seach for the directed grap.
        In depth first search we visit each node and its neighbour recusively.
        """
        self.__depth_first_search_direct_graph(vertex, set())

    def __depth_first_search_direct_graph(self, vertex: str, visited_nodes: set):
        """
        Recursive private method to visit the neighbouring node recursively.
        """
        # Visit the vertex and then add the vertex to the set.
        print(vertex)
        visited_nodes.add(vertex)
        # recursively visit its neighbour and if the vertex is not visited then visit it.
        if self.adj_list.get(vertex):
            for vertex in self.adj_list.get(vertex):
                for node in vertex:
                    if node not in visited_nodes:
                        self.__depth_first_search_direct_graph(
                            node, visited_nodes)
        else:
            raise AssertionError(f"{vertex} is not a valid vertex.")

    def breadth_first_search_directed_graph(self, vertex: str):
        """
        In breadth first seach we visit the node and all its neighbour before
        visiting other nodes.
        """
        if not self.adj_list.get(vertex):
            return
        # Initialize a set to keep track of visited nodes.
        # Initialize a set to add the not visited neighbours in the queue
        visited_nodes = set()
        queue = []
        queue.append(vertex)
        while len(queue) != 0:
            current_vertex = queue.pop(0)
            if current_vertex in visited_nodes:
                continue
            print(current_vertex)
            visited_nodes.add(current_vertex)
            for neighbour in self.adj_list.get(vertex):
                for node in neighbour:
                    if node not in visited_nodes:
                        queue.append(node)


graph = DirectedGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B', 2)
# graph.add_edge('A', 'C', 5)
graph.add_edge('C', 'D', 7)
# graph.remove_edge('A', 'B')
# graph.remove_edge('B', 'C')
# graph.remove_edge('B', 'D')
# graph.remove_vertex('A')
graph.breadth_first_search_directed_graph('C')
# graph.print_graph()
