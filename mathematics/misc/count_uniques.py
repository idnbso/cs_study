"""
Implement a function called count_uniques_values which accepts a sorted array and counts the unique
values in the array. There can be negative numbers in the array, but it will always be sorted.
"""


def count_uniques_values(nums):
    """
    T: O(N), S: O(2) = O(1)
    :param nums:
    :return:
    """
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


def count_uniques_values_naive(nums):
    """
    T: O(N), S: O(2) = O(1)
    :param nums:
    :return:
    """
    if not nums:
        return 0

    last_num = nums[0]
    total_uniques = 1

    for num in nums[1:]:
        if num != last_num:
            total_uniques += 1
            last_num = num

    return total_uniques


if __name__ == '__main__':
    print(count_uniques_values([1, 1, 1, 1, 1]))  # 1
    print(count_uniques_values([1, 1, 1, 1, 1, 2]))  # 2
    print(count_uniques_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))  # 7
    print(count_uniques_values([]))  # 0
    print(count_uniques_values([-2, -1, -1, 0, 1]))  # 4
