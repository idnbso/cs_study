"""
Creating pointers or values that correspond to an index or position and move tward the beginning,
end or middle based on a certain condition.

Very efficient for solving problems with minimal space complexity as well

write a function called sum_zero which accepts a sorted array of integers.
The function should find the first pair where the sum is 0.
Return an array that includes both values that sum to zero or None if a pair does not exist.
"""


def sum_zero(nums):
    """
    T: O(N/2) = O(N), S: O(1)
    :param nums: sorted array of integers
    :return: the first pair that sums to zero or none
    """
    i = 0
    j = len(nums) - 1

    while i < j:
        left = nums[i]
        right = nums[j]
        lr_sum = left + right

        if lr_sum == 0:
            return [left, right]
        elif lr_sum > 0:
            j -= 1
        else:
            i -= 1

    return None


def sum_zero_naive(nums):
    """
    T: O(N**2), S: O(1)
    :param nums:
    :return:
    """
    for i, num_a in enumerate(nums):
        for num_b in nums[i+1:]:
            if num_a + num_b == 0:
                return [num_a, num_b]
    return None


if __name__ == '__main__':
    print(sum_zero_naive([-2, 2, 4, 5, 6, 7]))
    print(sum_zero_naive([-3, -2, -1, 0, 1, 2, 3]))
    print(sum_zero_naive([-2, 0, 1, 3]))
    print(sum_zero_naive([1, 2, 3]))
