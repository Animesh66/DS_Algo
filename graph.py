class Graph:
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


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.print_graph()
