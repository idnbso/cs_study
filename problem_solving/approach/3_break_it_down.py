"""
Write a function which takes a string and returns counts of each character in the string.

Break It Down
* Explicitly write out the steps you need to take.
    This forces you to think about the code you'll write before you write ut, and helps you catch
    any lingering conceptual issues or misunderstandings before you dive in and have to worry about
    details as well.
"""


def get_char_count(string):
    # make object to return at the end
    counter = {}

    # loop over the string
    for char in string:
        char = str.lower(char)

        # only add lower cased characters to the dictionary
        if 'a' <= char <= 'z':
            counter[char] = counter[char] + 1 if char in counter else 1

    # return the result
    return counter


if __name__ == '__main__':
    print(get_char_count("Hello Man"))
