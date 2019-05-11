"""
This pattern involves dividing a data set into smaller chunks and then repeating a process with a
subset of data. This pattern can tremendously decrease time complexity.
"""


def binary_search(arr, target):
    """
    O(Log(n))
    :param arr:
    :param target:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        cur = arr[middle]

        if cur == target:
            return middle
        elif cur > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def binary_search_variant(arr, target):
    """
    O(Log(n))
    This variant demonstrates the usage of different indices and why len(arr) - 1 is preferred
    :param arr:
    :param target:
    :return:
    """
    n = len(arr)
    left_index = 0
    right_index = n
    mid_index = (left_index + right_index) // 2

    while mid_index < n - 1:
        mid = arr[mid_index]
        if mid == target:
            break
        elif mid > target:
            right_index = mid_index
        else:
            left_index = mid_index
        mid_index = (left_index + right_index) // 2

    return mid_index if arr[mid_index] == target else -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6], 4))  # 3
    print(binary_search([1, 2, 3, 4, 5, 6], 6))  # 5
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 6))  # 5
    print(binary_search([1, 2, 3, 4, 5, 6], 11))  # -1
