class BinarySearchTree:
    def __init__(self, node=None):
        self.root = node

    def insert(self, value):
        """
        O(log(n))
        :param value:
        :return:
        """
        node = Node(value)
        if not self.root:
            self.root = node
            return self

        parent = self.root
        while True:
            if parent.value > value:
                if not parent.left:
                    parent.left = node
                    return self
                parent = parent.left
            elif parent.value < value:
                if not parent.right:
                    parent.right = node
                    return self
                parent = parent.right
            else:
                return self

    def find(self, value):
        """
        O(log(n))
        :param value:
        :return:
        """
        if not self.root:
            return False

        cur = self.root
        while cur:
            if cur.value > value:
                cur = cur.left
            elif cur.value < value:
                cur = cur.right
            else:
                return cur

        return False

    def breadth_first_search(self, value):
        queue = [self.root]
        visited = []
        is_found = False

        while len(queue) > 0:
            cur = queue.pop(0)
            visited.append(cur.value)

            if cur.value == value:
                is_found = True
                break

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

        return {'visited': visited, 'is_found': is_found}

    def breadth_first_search_recursive(self, value, queue=None, visited=None):
        if queue is None and visited is None:
            queue = [self.root]
            visited = []

        if len(queue) == 0:
            return visited

        node = queue.pop(0)
        if node:
            visited.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            self.breadth_first_search_recursive(value, queue, visited)

        return visited

    def depth_first_search_iterative_pre_order(self, value):
        stack = [self.root]
        visited = []
        is_found = False
        while len(stack) > 0:
            cur = stack.pop()
            visited.append(cur.value)

            if cur.value == value:
                is_found = True
                break

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return {'visited': visited, 'is_found': is_found}

    def depth_first_search_recursive_pre_order(self, value, node=None, visited=None):
        if node is None and visited is None:
            node = self.root
            visited = []

        is_found = False
        result = {'visited': visited, 'is_found': is_found}
        if node:
            visited.append(node.value)
            if node.value == value or result['is_found']:
                result['is_found'] = True
                return result

            result = self.depth_first_search_recursive_pre_order(value, node.left, visited)
            if result['is_found']:
                return result

            result = self.depth_first_search_recursive_pre_order(value, node.right, visited)
        return result

    def depth_first_search_recursive_pre_order_alt(self, value):
        visited = []

        def traverse(node):
            visited.append(node.value)
            if node.value == value:
                return True

            if traverse(node.left) if node.left else False:
                return True

            return traverse(node.right) if node.right else False

        is_found = traverse(self.root)
        return {'visited': visited, 'is_found': is_found}

    def depth_first_search_iterative_in_order(self, value):
        stack = [self.root]
        visited = []
        is_found = False
        while len(stack) > 0:
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

            visited.append(cur.value)
            if cur.value == value:
                is_found = True
                break

        return {'visited': visited, 'is_found': is_found}

    def depth_first_search_recursive_in_order(self, value, node=None, visited=None):
        if node is None and visited is None:
            node = self.root
            visited = []

        is_found = False
        result = {'visited': visited, 'is_found': is_found}
        if node:
            result = self.depth_first_search_recursive_in_order(value, node.left, visited)
            visited.append(node.value)
            if node.value == value or result['is_found']:
                result['is_found'] = True
                return result

            result = self.depth_first_search_recursive_in_order(value, node.right, visited)
        return result

    def depth_first_search_recursive_post_order(self, value, node=None, visited=None):
        if node is None and visited is None:
            node = self.root
            visited = []

        is_found = False
        result = {'visited': visited, 'is_found': is_found}
        if node:
            result = self.depth_first_search_recursive_post_order(value, node.left, visited)
            if result['is_found']:
                return result

            result = self.depth_first_search_recursive_post_order(value, node.right, visited)

            visited.append(node.value)
            if node.value == value or result['is_found']:
                result['is_found'] = True
                return result
        return result

    def __repr__(self):
        return str(self.__dict__)


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    """
          10
      5       13
    2   7   11  16
    """
    tree = BinarySearchTree()
    tree.insert(10)
    print(tree)
    tree.insert(5)
    print(tree)
    tree.insert(13)
    print(tree)
    tree.insert(11)
    print(tree)
    tree.insert(2)
    print(tree)
    tree.insert(16)
    print(tree)
    tree.insert(7)
    print(tree)
    print(f'is 7 in tree: {tree.find(7)}')
    print(f'is 3 in tree: {tree.find(3)}')
    print(f'is 13 in tree: {tree.find(13)}')
    print(f'bfs iterative traversal: ${tree.breadth_first_search(11)}')
    print(f'bfs iterative traversal: ${tree.breadth_first_search(15)}')
    print(f'bfs recursive traversal: ${tree.breadth_first_search_recursive(11)}')
    print(f'bfs recursive traversal: ${tree.breadth_first_search_recursive(15)}')
    print(f'dfs iterative pre order: ${tree.depth_first_search_iterative_pre_order(11)}')
    print(f'dfs iterative pre order: ${tree.depth_first_search_iterative_pre_order(15)}')
    print(f'dfs recursive pre order: ${tree.depth_first_search_recursive_pre_order(11)}')
    print(f'dfs recursive pre order: ${tree.depth_first_search_recursive_pre_order(17)}')
    print(f'dfs recursive pre order alt: ${tree.depth_first_search_recursive_pre_order_alt(11)}')
    print(f'dfs recursive pre order alt: ${tree.depth_first_search_recursive_pre_order_alt(14)}')
    print(f'dfs recursive in order: ${tree.depth_first_search_recursive_in_order(11)}')
    print(f'dfs recursive in order: ${tree.depth_first_search_recursive_in_order(12)}')
    print(f'dfs recursive post order: ${tree.depth_first_search_recursive_post_order(11)}')
    print(f'dfs recursive post order: ${tree.depth_first_search_recursive_post_order(12)}')
