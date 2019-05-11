"""
Find the first longest substring of unique characters

"hellothere" => "lother"

"""


def find_longest_substring(string):
    """
    O(N)
    :param string:
    :return:
    """
    if not string:
        return ""

    longest_substring = ""
    cur_substring = ""
    cur_substring_counter = {}

    for i, char in enumerate(string):
        if char not in cur_substring_counter:
            cur_substring_counter[char] = True
            cur_substring += char
            longest_substring = max(longest_substring, cur_substring)
        else:
            cur_substring = char
            cur_substring_counter = {char: True}

    return longest_substring


if __name__ == '__main__':
    print(find_longest_substring("hellothere"))
    print(find_longest_substring("hello"))
    print(find_longest_substring("helo"))
    print(find_longest_substring("hhhhh"))
