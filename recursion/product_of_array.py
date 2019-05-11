def product_of_array(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]

    new_array = []
    for i in range(1, len(arr)):
        new_array.append(arr[i])

    return arr[0] * product_of_array(new_array)


def product_of_array_variant(arr, i=0):
    if not arr:
        return None

    if len(arr) - 1 == i:
        return arr[i]

    return arr[i] * product_of_array_variant(arr, i + 1)


if __name__ == '__main__':
    print(product_of_array([1, 2, 3]))  # 6
    print(product_of_array([1]))  # 1
    print(product_of_array([0]))  # None
    print(product_of_array([]))  # None
