class StackDoubleLinkedList:
    def __init__(self, top=None):
        self.top = top
        self.length = 1 if top else 0

    def push(self, value):
        node = Node(value)

        if self.top:
            self.top.next = node
            node.prev = self.top

        self.top = node
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.prev
        self.length -= 1
        return node.value

    def peek(self):
        return self.top.value

    def get_array(self):
        arr = []
        cur = self.top
        while cur:
            arr.append(cur.value)
            cur = cur.prev
        return arr

    def __str__(self):
        return str(self.get_array())


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    stack = StackDoubleLinkedList()
    stack.push('A').push('B').push('C')
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
