"""
Closest Number

Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by
M. If there are more than one such number, then output the one having maximum absolute value.

Input:
The first line consists of an integer T i.e number of test cases. T testcases follow.  The first and
 only line of each test case contains two space separated integers N and M.

Output:
For each testcase, in a new line, print the closest number to N which is also divisible by M.

Constraints:
1 <= T <= 100
-1000 <= N, M <= 1000

Example:
Input:
2
13 4
-15 6
Output:
12
-18

"""


def closest_number(n, m):
    return (n // m) * m


def closest_number_brute(n, m):
    pass


if __name__ == '__main__':
    total_inputs = int(input())
    for inp in range(total_inputs):
        inp_n, inp_m = [int(x) for x in input().split()]
        print(closest_number(inp_n, inp_m))
