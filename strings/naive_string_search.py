"""
Suppose you want to count the number of times a smaller string appears in a longer string.

A straightforward approach involves checking pairs of characters individually.

"""


def naive_string_search(string, pattern):
    """
    O(N)
    :param string:
    :param pattern:
    :return:
    """
    counter = 0

    for string_iter in range(len(string) - len(pattern) + 1):
        is_found = True
        for pattern_iter in range(len(pattern)):
            if string[string_iter + pattern_iter] != pattern[pattern_iter]:
                is_found = False
                break

        if is_found:
            counter += 1

    return counter


def naive_string_search_variant_b(string, pattern):
    """
    O(N)
    :param string:
    :param pattern:
    :return:
    """
    counter = 0
    string_iter = 0
    pattern_iter = 0

    while string_iter < len(string):
        if string[string_iter] == pattern[pattern_iter]:
            pattern_iter += 1
        else:
            pattern_iter = 0

        if pattern_iter == len(pattern):
            counter += 1
            string_iter -= pattern_iter - 1
            pattern_iter = 0

        string_iter += 1

    return counter


if __name__ == '__main__':
    print(naive_string_search("harold said haha in hamburg haha", "haha"))  # 2
    print(naive_string_search("wowomgzomgwwomg", "omg"))  # 3
    print(naive_string_search("wowomgzomgwwomg", "berg"))  # 0
    print(naive_string_search("aaaaaa", "aa"))  # 5
    print(naive_string_search("lorie loled", "lo"))  # 2
