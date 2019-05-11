class Queue:
    def __init__(self, first=None):
        self.first = first
        self.last = self.first
        self.size = 1 if first else 0

    def enqueue(self, value):
        """
        O(1)
        :param value:
        :return:
        """
        node = Node(value)
        if self.size == 0:
            self.first = node
        else:
            self.last.next = node

        self.last = node
        self.size += 1
        return self

    def dequeue(self):
        """
        O(1)
        :return:
        """
        if self.size == 0:
            return None

        node = self.first
        if self.first == self.last:
            self.last = None

        self.first = node.next
        self.size -= 1
        return node.value

    def peek(self):
        return self.first.value if self.first else None

    def get_array(self):
        arr = []
        cur = self.first
        while cur:
            arr.append(cur.value)
            cur = cur.next

        return arr

    def __str__(self):
        return str(self.get_array())


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    q = Queue()
    q.enqueue('A').enqueue('B').enqueue('C')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.peek())
