"""
ANAGRAMS
Given two strings, write a function to determine if the second string is an anagram of the first.
an anagram is word, phrase or name formed by rearranging the letters of another.

Examples:
    cinema => iceman

"""


def is_anagram(str_a, str_b):
    """
    O(2n+c) = O(n)
    :param str_a:
    :param str_b:
    :return:
    """
    if len(str_a) != len(str_b):
        return False

    str_a_counter = get_char_counter(str_a)
    str_b_counter = get_char_counter(str_b)

    for char, frq in str_a_counter.items():
        if char not in str_b_counter or str_b_counter[char] != frq:
            return False

    return True


def is_anagram_improved(str_a, str_b):
    """
    O(2n) = O(n)
    :param str_a:
    :param str_b:
    :return:
    """
    if len(str_a) != len(str_b):
        return False

    str_a_counter = get_char_counter(str_a)

    for char in str_b:
        if not str_a_counter[char]:
            return False
        str_a_counter[char] -= 1

    return True


def get_char_counter(str_i):
    counter = {}

    for char in str_i:
        char = str.lower(char)
        counter[char] = counter[char] + 1 if char in counter else 1

    return counter


if __name__ == '__main__':
    print(is_anagram_improved("cinema", "iceman"))
