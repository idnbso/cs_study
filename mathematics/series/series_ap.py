"""
Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term of the series.

Input:
The first line of input contains an integer, the number of test cases T. T testcases follow. Each testcase in its first line should contain two positive integer A and B(First 2 terms of AP). In the second line of every testcase it contains of an integer N.

Output:
For each testcase, in a new line, print the Nth term of the Arithmetic Progression.

Constraints:
1 <= T <= 100
-103 <= A <= 103
-103 <= B <= 103
1 <= N <= 104

Example:
Input:
2
2 3
4
1 2
10

Output:
5
10
"""


def get_series_ap_term(n, a, b):
    """
    O(1)
    """
    diff = b - a
    return a + (n-1)*diff


def get_series_ap_term_brute(n, a, b):
    """
    O(n-1) = O(n)
    """
    diff = b - a
    term = a
    for i in range(1, n):
        term += diff
    return term


if __name__ == '__main__':
    total_inputs = int(input())
    for inp in range(total_inputs):
        inp_num_a, inp_num_b = [int(x) for x in input().split()]
        inp_n = int(input())
        print(get_series_ap_term_brute(inp_n, inp_num_a, inp_num_b))
