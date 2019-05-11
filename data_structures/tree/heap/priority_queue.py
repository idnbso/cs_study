from data_structures.tree.heap.min_binary_heap import MinBinaryHeap


class PriorityQueue:
    def __init__(self, value=None, priority=None):
        node = Node(value, priority)
        self.heap = MinBinaryHeap(node)

    def enqueue(self, value, priority):
        """
        O(log(n))
        :param value:
        :param priority:
        :return:
        """
        node = Node(value, priority)
        self.heap.insert(node)
        return self

    def dequeue(self):
        """
        O(log(n))
        :return:
        """
        return self.heap.extract_min()

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)


class Node:
    def __init__(self, value=None, priority=0):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    p = PriorityQueue()
    p.enqueue('A', 3).enqueue('B', 1).enqueue('C', 2).enqueue('D', 5).enqueue('E', 4)
    print(p)
    print(p.dequeue())
    print(p.dequeue())
    print(p)
    print(p.dequeue())
    print(p.dequeue())
    print(p.dequeue())
    print(p.dequeue())
