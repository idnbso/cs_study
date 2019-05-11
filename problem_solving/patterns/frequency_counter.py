"""
This pattern uses objects or sets to collect values/frequencies of values

This can often avoid the need for nested loops or O(N^2) operations with arrays / strings
"""


def same_brute_force_loops(src_array, sq_array):
    """
    O(N**2)
    :param src_array: the source array
    :param sq_array: the squared source array
    :return: are the arrays the same
    """
    if len(src_array) != len(sq_array):
        return False

    sq_array_copy = sq_array.copy()

    for num_a in src_array:
        is_found_sq = False
        if num_a**2 not in sq_array_copy:
            return False
        sq_array_copy.remove(num_a**2)

        for num_b in sq_array_copy:
            if num_a**2 == num_b:
                is_found_sq = True
                sq_array_copy.remove(num_b)
                break

        if not is_found_sq:
            return False

    return True


def same_brute_force(src_array, sq_array):
    """
    O(N**2)
    :param src_array: the source array
    :param sq_array: the squared source array
    :return: are the arrays the same
    """
    if len(src_array) != len(sq_array):
        return False

    sq_array_copy = sq_array.copy()

    for num_a in src_array:
        if num_a**2 not in sq_array_copy:
            return False
        sq_array_copy.remove(num_a**2)

    return True


def same(src_array, sq_array):
    """
    O(3n)=O(n)
    :param src_array: the source array
    :param sq_array: the squared source array
    :return: are the arrays the same
    """
    if len(src_array) != len(sq_array):
        return False

    src_counter = {}
    sq_counter = {}

    for num in src_array:
        src_counter[num] = src_counter[num] + 1 if num in src_counter else 1

    for num in sq_array:
        sq_counter[num] = sq_counter[num] + 1 if num in sq_counter else 1

    for num, frq in src_counter.items():
        if num**2 not in sq_counter or sq_counter[num**2] != frq:
            return False

    return True


if __name__ == '__main__':
    print(same([1, 2, 3, 2], [1, 4, 4, 9]))
