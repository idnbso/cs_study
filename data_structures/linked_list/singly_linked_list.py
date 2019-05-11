class SinglyLinkedList:
    def __init__(self, value=None):
        head = None if not value else Node(value)
        self.head = head
        self.tail = head
        self.length = 0 if not head else 1

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return self

    def insert(self, index, value):
        node = Node(value)

        if index > self.length:
            return None
        elif index == self.length - 1:
            return self.push(value)
        elif index == 0:
            return self.unshift(value)

        pre = self.get(index - 1)
        node.next = pre.next
        pre.next = node
        self.length += 1
        return node

    @staticmethod
    def insert_after(prev_node, value):
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return new_node

    def insert_variant(self, index, value):
        node = Node(value)

        if index > self.length:
            return None

        cur = self.head
        for i in range(0, index - 1):
            cur = cur.next

        node.next = cur.next
        cur.next = node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.shift()

        pre = self.get(index - 1)
        node = self.get(index)
        pre.next = node.next
        self.length -= 1
        return node

    def pop(self):
        return self.remove(self.length - 1)

    def pop_variant(self):
        if not self.head:
            return None

        cur = self.head
        new_tail = cur

        while cur.next:
            new_tail = cur
            cur = cur.next

        new_tail.next = None
        self.tail = new_tail
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return cur

    def shift(self):
        """
        Shifts to the left one element and returns it.
        :return: the head of the list
        """
        if self.length == 0:
            return None

        node = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return node

    def unshift(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return node

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        cur = self.head
        for cur_index in range(1, index + 1):
            cur = cur.next

        return cur

    def set(self, index, value):
        node = self.get(index)

        if not node:
            return None

        node.value = value
        return node

    def get_array(self):
        arr = []
        cur = self.head
        for i in range(self.length):
            arr.append(cur.value)
            cur = cur.next
        return arr

    def __str__(self):
        return ' -> '.join(self.get_array()) + ' -> None'


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    my_list = SinglyLinkedList()
    my_list.push("Hello").push("World").push("Goodbye")
    print(my_list)
    print(my_list.get(0))
    print(my_list.get(2))
    print(my_list.pop())
    print(my_list)
    print(my_list.shift())
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.unshift("World"))
    print(my_list.insert(0, 'OMG'))
    print(my_list.insert(2, 'ZOMG'))
    print(my_list)
    print(my_list.remove(2))
    print(my_list)
    print(my_list.push('ZOMG'))
    print(my_list.reverse())
