"""
Write a function which takes in a string and returns counts of each character in the string.

Explore Examples:
* Start with simple and straight forward examples.
* Progress to more complex examples.
* Explore examples with empty inputs.
* Explore examples with invalid inputs.

Examples:
    Simple:
    char_count("aaaa") => { a: 4 }
    char_count("hello") => { h: 1, e: 1, l: 2, o: 1 }

    Complex:
    char_count("my phone number is 18232332")
    char_count("Hello hi")

    Empty Inputs:
    char_count("") => {}
    char_count()

"""


def char_count(word):
    counter = {}
    for char in word:
        counter[char] = counter[char] + 1 if char in counter else 1
    return counter


if __name__ == '__main__':
    print(char_count("hello"))
