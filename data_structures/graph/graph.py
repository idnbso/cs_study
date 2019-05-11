class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        return self

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return self

        neighbours = self.adjacency_list[vertex]
        for i, neighbour in enumerate(neighbours):
            self.remove_edge(neighbour, vertex)

        self.adjacency_list.pop(vertex)
        return self

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list or to_vertex not in self.adjacency_list:
            return self

        if to_vertex not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(to_vertex)

        if from_vertex not in self.adjacency_list[to_vertex]:
            self.adjacency_list[to_vertex].append(from_vertex)
        return self

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list or to_vertex not in self.adjacency_list:
            return self

        self.adjacency_list[from_vertex] = list(filter(lambda v: v != to_vertex,
                                                       self.adjacency_list[from_vertex]))
        self.adjacency_list[to_vertex] = list(filter(lambda v: v != from_vertex,
                                                     self.adjacency_list[to_vertex]))
        return self

    def depth_first_search_recursive(self, start_vertex):
        traversal = []
        visited = {}

        def dfs(vertex):
            if vertex is None:
                return
            traversal.append(vertex)
            visited[vertex] = True
            neighbors = self.adjacency_list[vertex]
            for index, neighbor in enumerate(neighbors):
                if neighbor not in visited or visited[vertex] is False:
                    dfs(neighbor)

        dfs(start_vertex)
        return traversal

    def depth_first_search_iterative(self, start_vertex):
        result = []
        visited = {start_vertex: True}
        stack = [start_vertex]
        while len(stack) > 0:
            vertex = stack.pop()
            result.append(vertex)
            neighbors = self.adjacency_list[vertex]
            for index, neighbor in enumerate(neighbors):
                if neighbor not in visited or visited[neighbor] is False:
                    stack.append(neighbor)
                    visited[neighbor] = True

        return result

    def breadth_first_search_iterative(self, start_vertex):
        result = []
        visited = {start_vertex: True}
        queue = [start_vertex]
        while len(queue) > 0:
            vertex = queue.pop(0)
            result.append(vertex)
            neighbors = self.adjacency_list[vertex]
            for index, neighbor in enumerate(neighbors):
                if neighbor not in visited or visited[neighbor] is False:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def __repr__(self):
        return str(self.adjacency_list)


if __name__ == '__main__':
    """
       A
     /  \
    B    C
    |    |
    D -- E
     \  /
      F
    """
    g = Graph()
    g.add_vertex('A').add_vertex('B').add_vertex('C').add_vertex('D').add_vertex('E') \
        .add_vertex('F')
    g.add_edge('A', 'B').add_edge('A', 'C').add_edge('B', 'D').add_edge('C', 'E') \
        .add_edge('D', 'E').add_edge('D', 'F').add_edge('E', 'F')
    print(g)
    print(g.depth_first_search_recursive('A'))
    print(g.depth_first_search_iterative('A'))
    print(g.breadth_first_search_iterative('A'))
