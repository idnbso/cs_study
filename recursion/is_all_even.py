def is_all_even(nums, i=0):
    if len(nums) == i:
        return True

    if nums[i] % 2 != 0:
        return False

    return True and is_all_even(nums, i + 1)


if __name__ == '__main__':
    print(is_all_even([1, 2, 3]))
    print(is_all_even([2, 1, 3]))
    print(is_all_even([2, 2, 2]))
    print(is_all_even([2, 4, 6]))
