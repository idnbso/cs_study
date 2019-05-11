class MaxBinaryHeap:
    def __init__(self, value=None):
        self.values = []
        if value:
            self.values.append(value)

    def insert(self, value):
        self.values.append(value)
        self.bubble_up(len(self.values) - 1)
        return self

    def bubble_up(self, index):
        cur_index = index
        parent_index = self.get_parent_index(cur_index)
        while parent_index >= 0 and self.values[parent_index] < self.values[cur_index]:
            self.swap_nodes(parent_index, cur_index)
            cur_index = parent_index
            parent_index = self.get_parent_index(cur_index)

    def extract_max(self):
        if len(self.values) == 0:
            return None

        max_value = self.values[0]
        last = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = last
            self.bubble_down(0)
        return max_value

    def bubble_down(self, index):
        while True:
            value = self.values[index]
            left_index = self.get_left_child_index(index)
            right_index = self.get_right_child_index(index)

            if left_index > len(self.values) - 1:
                break

            left = self.values[left_index]
            right = None
            if right_index <= len(self.values) - 1:
                right = self.values[right_index]

            if value < left and (right is None or left > right):
                self.swap_nodes(index, left_index)
                index = left_index
            elif right is not None and value < right and right > left:
                self.swap_nodes(index, right_index)
                index = right_index
            else:
                break

    def swap_nodes(self, first_index, second_index):
        second = self.values[second_index]
        self.values[second_index] = self.values[first_index]
        self.values[first_index] = second

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    @staticmethod
    def get_right_child_index(parent_index):
        return 2 * parent_index + 2

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)


if __name__ == '__main__':
    mbh = MaxBinaryHeap()
    mbh.insert(41)
    mbh.insert(39)
    mbh.insert(33)
    mbh.insert(18)
    mbh.insert(27)
    print(mbh.insert(12))
    print(mbh.insert(55))
    print(mbh.insert(20))
    while len(mbh) > 0:
        print(mbh.extract_max())
        print(mbh)
    print(mbh.extract_max())
    print(mbh)
