"""
Write a function called max_subarray_sum which accepts an array of integers an a number called n.
The function should calculate the maximum sum of n consecutive elements in the array.
"""
import math


def max_subarray_sum(nums, n):
    """
    O(n)
    :param nums:
    :param n:
    :return:
    """
    if n > len(nums):
        return None

    max_sum = 0

    # sum the first subarray
    for i in range(n):
        max_sum += nums[i]

    # assign the first max sum as the first sliding window
    temp_sum = max_sum

    for i in range(len(nums) - n):
        temp_sum = (temp_sum - nums[i]) + nums[i+n]
        max_sum = max(temp_sum, max_sum)

    return max_sum


def max_subarray_sum_variation(nums, n):
    """
    O(n)
    :param nums:
    :param n:
    :return:
    """
    if n > len(nums):
        return None

    max_sum = 0

    # sum the first subarray
    for i in range(n):
        max_sum += nums[i]

    # assign the first max sum as the first sliding window
    temp_sum = max_sum

    for i in range(n, len(nums)):
        temp_sum = (temp_sum - nums[n - i]) + nums[i]
        if temp_sum > max_sum:
            max_sum = temp_sum

    return max_sum


def max_subarray_sum_naive(nums, n):
    """
    n = len(nums), M = n
    O((N-M+1)*M) = O((N - N**0.5 + 1) * N**0.5) = O(N*N**0.5) = O(N**1.5) = O(N**2)
    :param nums:
    :param n:
    :return:
    """
    if n > len(nums):
        return None

    max_sum = -math.inf
    for i in range(0, len(nums) - n + 1):
        cur_sum = nums[i]
        for j in range(1, n):
            cur_sum += nums[i + j]

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


def max_subarray_sum_alternative(nums, n):
    """
    O(n)
    :param nums:
    :param n:
    :return:
    """
    if n > len(nums):
        return None

    max_sum = -math.inf
    for i in range(0, len(nums) - n + 1):
        cur_sum = nums[i]
        if i + 1 < len(nums):
            for j in range(i + 1, i + n):
                cur_sum += nums[j]

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


if __name__ == '__main__':
    print(max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 2))  # 10
    print(max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 4))  # 17
    print(max_subarray_sum([4, 2, 1, 6], 1))  # 6
    print(max_subarray_sum([4, 2, 1, 6, 2], 4))  # 13
    print(max_subarray_sum([], 4))  # None
    print(max_subarray_sum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))  # 6
