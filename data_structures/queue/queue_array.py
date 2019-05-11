class QueueArray:
    def __init__(self, value=None):
        self.queue = []
        if value:
            self.queue.append(value)

    def enqueue(self, value):
        """
        O(N)
        :param value:
        :return:
        """
        self.queue.append(value)
        return self

    def dequeue(self):
        """
        O(N)
        :return:
        """
        if self.length() == 0:
            return None

        value = self.queue[0]
        for i in range(self.length() - 1):
            self.queue[i] = self.queue[i + 1]

        self.queue.pop()
        return value

    def length(self):
        return self.queue.__len__()

    def peek(self):
        return self.queue[0] if self.length() > 0 else None

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    queue = QueueArray()
    queue.enqueue('A').enqueue('B').enqueue('C')
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.peek())
