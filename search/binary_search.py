def binary_search(arr, target):
    """
    O(LOG(N))
    :param arr:
    :param target:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        cur = arr[middle]

        if cur > target:
            right = middle - 1
        elif cur < target:
            left = middle + 1
        else:
            return middle

    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6], 4))  # 3
    print(binary_search([1, 2, 3, 4, 5, 6], 6))  # 5
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 6))  # 5
    print(binary_search([1, 2, 3, 4, 5, 6], 11))  # -1
