def sum_of_range(x):
    if not x:
        return 0

    return x + sum_of_range(x - 1)


if __name__ == '__main__':
    print(sum_of_range(3))  # 6
    print(sum_of_range(1))  # 1
    print(sum_of_range(0))  # None
    print(sum_of_range(5))  # 15
