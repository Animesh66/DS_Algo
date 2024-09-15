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
            # if the vertex is not visited then print(visit) the vertex and add it to the set of visited vertex.
            print(current)
            visited_vertex.add(current)
            # visit the unvisited neighbour vertices using a for loop
            for neighbour in self.adj_list.get(current):
                if neighbour not in visited_vertex:
                    stack.append(neighbour)

    def bfs_traverse_directed_graph(self, vertex: str) -> None:
        """
        breadth first traversal of a directed graph
        This method will traverse the graph from any given node to its neightbour.
        """
        # first verify if the node exists or not.
        if not self.__verify_vertices_exists([vertex]):
            return
        # if the vertex is a valid vertex then create a set of visited vertex and a queue to track the list of all neighbours.
        visited_vertex = set()
        queue = []
        #  first put the vertex in the queue.
        queue.append(vertex)
        # Run the iterative loop while the queue is not empty.
        while len(queue) > 0:
            # first put deque the first element fro th queue.
            current = queue.pop(0)
            # verify if that queue is not in the visited vertex. If present the start the loop again.
            if current in visited_vertex:
                continue
            # if the vertex is not visted the visit the vetex and put the vertex in the visted vertex set.
            print(current)
            visited_vertex.add(current)
            # after that visit all the non visited neighbours.
            for neighbour in self.adj_list.get(current):
                if neighbour not in visited_vertex:
                    queue.append(neighbour)

    def topological_sort(self) -> list[str]:
        """
        This method will topologically sort all the vertex
        """
        # we need a set of all visited vertex and a stack to stack each items.
        visited_vertex = set()
        stack = list()
        # Now we need to visit all the nodes and perfrom a depth first traversal of each nodes.
        for vertex in self.adj_list.keys():
            self.__topological_sort(vertex, visited_vertex, stack)
        # Now the stack is populated in reverse order and we need to put these elements in a list
        sorted = list()
        while len(stack) > 0:
            sorted.append(stack.pop())
        return sorted

    def __topological_sort(self, vertex: str, visited_vertex, stack) -> None:
        """
        This is a recursive helper method to call from the public topological sort method.
        """
        # check if the node is visted then return.(base condition)
        if vertex in visited_vertex:
            return
        #  if the node is not visited then add it into the set.
        visited_vertex.add(vertex)
        # now visit all the non visted neighbours.
        for neighbour in self.adj_list.get(vertex):
            self.__topological_sort(neighbour, visited_vertex, stack)

        stack.append(vertex)

    def has_cycle(self) -> bool:
        """
        This method will return true if the directed graph has cycle otherwise return false.
        """
        #  Create 3 sets to keep track of all, visitig and visted nodes.
        all = set()
        visiting = set()
        visited = set()
        #  add all the nodes in the all set.
        for vertex in self.adj_list.keys():
            all.add(vertex)
        # Now pick a node from all of the nodes and perform a depth first search to all its neighbour
        while (len(all) > 0):
            # current value is the first element in the set.
            current = list(all)[0]
            if self.__has_cycle(current, all, visiting, visited):
                return True

        return False

    def __has_cycle(self, vertex: str,
                    all: set[str],
                    visiting: set[str],
                    visited: set[str]) -> bool:
        """
        This private method will be called from the has cycle method in a recursive way.
        """
        # First pick the current node from all and put it in the visitng set.
        all.remove(vertex)
        visiting.add(vertex)
        # Now we need to visit all the neighbours of this node.
        for neighbour in self.adj_list.get(vertex):
            # if the neighbour is in the visited set then continue checking next neighbour
            if neighbour in visited:
                continue
            #  if the neighbour is in the visiting set then it means we have a cycle
            if neighbour in visiting:
                return True
            #  Otherwise visit all neighbour recurively.
            result = self.__has_cycle(neighbour, all, visiting, visited)
            # if the reesult is true then no need to visit other neighbours.
            if result:
                return True
        # if we visited all the neighbours and does not return that means we do not ahve a cycle and we need to move the nodes from visiting set to visted set.
        visiting.remove(vertex)
        visited.add(vertex)
        return False


graph = DirectGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
# graph.add_vertex('P')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
# graph.add_edge('B', 'P')
# graph.remove_edge('A', 'B')
# graph.remove_vertex('A')
# graph.print_graph()
# graph.dfs_traversal_directed_graph('G')
# graph.dfs_traverse_non_recursive('C')
# graph.bfs_traverse_directed_graph('H')
# print(graph.topological_sort())
print(graph.has_cycle())
