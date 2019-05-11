class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        O(N)
        :param value:
        :return:
        """
        if len(self.stack) == 0:
            self.stack.append(value)
            return self

        prev = self.stack[0]
        self.stack[0] = value
        for index in range(1, len(self.stack)):
            cur = self.stack[index]
            self.stack[index] = prev
            prev = cur

        self.stack.append(prev)
        return self

    def pop(self):
        """
        O(N)
        :return:
        """
        if len(self.stack) == 0:
            return None

        value = self.stack[0]

        for index in range(len(self.stack) - 1):
            self.stack[index] = self.stack[index + 1]

        self.stack.pop()

        return value

    def peek(self):
        """
        O(1)
        :return:
        """
        return self.stack[0] if len(self.stack) > 0 else None

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack = StackArray()
    stack.push('A').push('B').push('C')
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
