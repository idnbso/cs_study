from math import inf
from data_structures.tree.heap.priority_queue import PriorityQueue


class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list or self.adjacency_list[vertex] is None:
            self.adjacency_list[vertex] = []
        return self

    def add_edge(self, from_vertex, to_vertex, weight):
        self.adjacency_list[from_vertex].append(Node(to_vertex, weight))
        self.adjacency_list[to_vertex].append(Node(from_vertex, weight))
        return self

    def get_shortest_path_by_dijkstra(self, start_vertex, end_vertex):
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return None

        priority_queue = PriorityQueue(start_vertex, 0)
        previous = {start_vertex: None}
        distances = {start_vertex: 0}
        for vertex_name, vertex_weight in self.adjacency_list.items():
            if vertex_name == start_vertex:
                continue

            distances[vertex_name] = inf
            priority_queue.enqueue(vertex_name, inf)

        while len(priority_queue) > 0:
            vertex = priority_queue.dequeue().value
            neighbors = self.adjacency_list[vertex]
            for i, neighbor in enumerate(neighbors):
                distance = distances.get(vertex) + neighbor.weight
                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    previous[neighbor.name] = vertex
                    priority_queue.enqueue(neighbor.name, distance)

        visited = [end_vertex]
        cur = end_vertex
        while cur != start_vertex:
            prev = previous[cur]
            visited.insert(0, prev)
            cur = prev
        return visited

    def __str__(self):
        return str(self.adjacency_list)


class Node:
    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    wg = WeightedGraph()
    wg.add_vertex('A').add_vertex('B').add_vertex('C').add_vertex('D').add_vertex('E') \
        .add_vertex('F')
    print(wg)
    wg.add_edge('A', 'B', 4).add_edge('A', 'C', 2).add_edge('B', 'E', 3).add_edge('E', 'D', 3) \
        .add_edge('C', 'D', 2).add_edge('C', 'F', 4).add_edge('D', 'F', 1).add_edge('E', 'F', 1)
    print(wg)
    print(wg.get_shortest_path_by_dijkstra('A', 'E'))
