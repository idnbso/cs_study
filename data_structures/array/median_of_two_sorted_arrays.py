import math

"""
Find the median of two sorted arrays.

eg.
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

median(arr1, arr2) = 3.5
"""


class Subarray:
    underlying = []
    start = 0
    size = 0

    @staticmethod
    def get_subarray_from_array(arr):
        subarray = Subarray()
        subarray.underlying = arr
        subarray.start = 0
        subarray.size = len(arr)
        return subarray

    def get_subarray(self, start, end):
        if start > end:
            raise ValueError('start index must be less than end index')
        if end > self.size:
            raise IndexError("index is out of bound")

        subarray = Subarray()
        subarray.underlying = self.underlying
        subarray.start = self.start + start
        subarray.size = end - start
        return subarray

    def get_size(self):
        return self.size

    def get_first(self):
        return self.underlying[self.start]

    def get_last(self):
        return self.underlying[self.start + (self.size - 1)]

    def get_median(self):
        if self.size % 2 == 0:
            return (self.underlying[self.start + ((self.size // 2) - 1)] +
                    self.underlying[self.start + (self.size // 2)]) / 2
        return self.underlying[self.start + (self.size // 2)]


def median_of_arrays_with_same_lengths(arr1, arr2):
    if len(arr1) == 0 or len(arr1) != len(arr2):
        raise ValueError('arrays must be of the same length')

    sarr1 = Subarray.get_subarray_from_array(arr1)
    sarr2 = Subarray.get_subarray_from_array(arr2)
    return median_of_subarrays_with_same_lengths(sarr1, sarr2)


def median_of_subarrays_with_same_lengths(sarr1, sarr2):
    if sarr1.get_size() == 1:
        return (sarr1.get_first() + sarr2.get_first()) / 2
    if sarr1.get_size() == 2:
        return (max(sarr1.get_first(), sarr2.get_first()) +
                min(sarr2.get_last(), sarr1.get_last())) / 2

    median1 = sarr1.get_median()
    median2 = sarr2.get_median()

    if median1 == median2:
        return median1
    elif median1 > median2:
        return median_of_subarrays_with_same_lengths(
            sarr1.get_subarray(0, sarr1.get_size() // 2 + 1),
            sarr2.get_subarray((sarr2.get_size() - 1) // 2, sarr2.get_size()))
    return median_of_subarrays_with_same_lengths(
        sarr1.get_subarray((sarr1.get_size() - 1) // 2, sarr1.get_size()),
        sarr2.get_subarray(0, sarr2.get_size() // 2 + 1))


def median_of_arrays_brute_force(arr1, arr2):
    """
    O(m+r) = O(n), S(n)
    :param arr1:
    :param arr2:
    :return:
    """
    arr1_idx = 0
    arr2_idx = 0
    cur_merge_idx = 0
    total_elements = len(arr1)
    total_merged_elements = total_elements * 2
    merge = []

    while cur_merge_idx < total_merged_elements:
        num1 = arr1[arr1_idx] if arr1_idx < total_elements else math.inf
        num2 = arr2[arr2_idx] if arr2_idx < total_elements else math.inf

        if num1 < num2:
            arr1_idx += 1
            num = num1
        else:
            arr2_idx += 1
            num = num2

        cur_merge_idx += 1
        merge.append(num)

    med1 = merge[total_merged_elements // 2 - 1]
    med2 = merge[total_merged_elements // 2]

    return (med1 + med2) / 2


if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    print(median_of_arrays_with_same_lengths(arr1, arr2))
