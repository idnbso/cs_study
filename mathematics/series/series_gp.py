"""
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case in its first line contains two positive integer A and B (First 2 terms of GP). In the second line of every test case it contains of an integer N.

Output:
In each seperate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

Constraints:
1 <= T <= 30
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Example:
Input:
2
2 3
1
1 2
2

Output:
2
2

Explanation:
Testcase 2: The second term of series whose common ratio is 2 will be 2.
"""
import math


def get_series_gp_term(n, a, b):
    """
    O(1)
    """
    ratio = b / a
    return math.floor(a * (ratio**(n-1)))


def get_series_gp_term_brute(n, a, b):
    """
    O(n-1) = O(n)
    """
    ratio = b / a
    term = a
    for i in range(1, n):
        term *= ratio
    return math.floor(term)


if __name__ == '__main__':
    total_inputs = int(input())
    for inp in range(total_inputs):
        inp_num_a, inp_num_b = [int(x) for x in input().split()]
        inp_n = int(input())
        print(get_series_gp_term(inp_n, inp_num_a, inp_num_b))
