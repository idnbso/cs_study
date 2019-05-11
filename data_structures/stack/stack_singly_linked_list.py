class Stack:
    def __init__(self, top=None):
        self.top = top
        self.tail = top
        self.length = 1 if top else 0

    def push(self, value):
        """
        O(1)
        :param value:
        :return:
        """
        node = Node(value)

        if not self.top:
            self.tail = self.top = node
        else:
            node.next = self.top
            self.top = node

        self.length += 1
        return self

    def pop(self):
        """
        O(1)
        :return:
        """
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next

        if self.top == self.tail:
            self.tail = None

        self.length -= 1
        return node.value

    def peek(self):
        return self.top.value

    def get_array(self):
        arr = []

        cur = self.top
        while cur:
            arr.append(cur.value)
            cur = cur.next
        return arr

    def __str__(self):
        return str(self.get_array())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    stack = Stack()
    stack.push('A').push('B').push('C')
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
