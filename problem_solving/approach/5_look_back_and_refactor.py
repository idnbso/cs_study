"""
REFACTORING QUESTIONS
Can you check the result?
Can you derive the result differently?
Can you understand it at a glance?
Can you use the result or method for some other problem?
Can you improve the performance of your solution?
Can you think of other ways to refactor?
How have other people solved this problem?
"""


def get_char_count(string):
    # make object to return at the end
    counter = {}

    # loop over the string
    for char in string:
        # only add lower cased characters to the dictionary
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            char = str.lower(char)
            counter[char] = counter[char] + 1 if char in counter else 1

    # return the result
    return counter


if __name__ == '__main__':
    print(get_char_count("Hello World!!1"))
