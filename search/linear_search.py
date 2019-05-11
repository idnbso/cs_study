def linear_search(arr, target):
    """
    O(N)
    :param arr:
    :param target:
    :return:
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6], 4))  # 3
    print(linear_search([1, 2, 3, 4, 5, 6], 6))  # 5
    print(linear_search(['1', '2', '3', '4', '5', '6', '7'], '6'))  # 5
    print(linear_search([1, 2, 3, 4, 5, 6], 11))  # -1
