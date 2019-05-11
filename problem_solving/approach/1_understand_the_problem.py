"""
Write a function which takes two numbers and returns their sum.

1. Can I restate the problem in my own words?
    Implement addition.
2. What are the inputs that go into the problem?
    ints? floats? what about strings for large numbers?
3. What are the outputs that should come from the solution to the problem?
    int? float? string?
4. Can the outputs be determined from the inputs? In other words, do I have enough information to
   solve problem?
    There has to be two input parameters for addition, else if only one then just return the number.
5. How should I label the important pieces of data that are a part of the problem?
    the input parameters are num_a and num_b, the addition result is returned as is,

"""


def sum_of_two(num_a, num_b):
    return num_a + num_b


if __name__ == '__main__':
    print(sum_of_two(2, 3))
