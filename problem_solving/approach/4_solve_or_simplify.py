"""
Write a function which takes a string and returns counts of each character in the string.

Simplify
* Find the core difficulty in what you are trying to do.
* Temporarily ignore that difficulty.
* Write a simplified solution
* Then incorporate that difficulty back in.
"""


def get_char_count(string):
    # make object to return at the end
    counter = {}

    # loop over the string
    for char in string:
        char = str.lower(char)

        # only add lower cased characters to the dictionary
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            counter[char] = counter[char] + 1 if char in counter else 1

    # return the result
    return counter


if __name__ == '__main__':
    print(get_char_count("Hello World!!1"))
