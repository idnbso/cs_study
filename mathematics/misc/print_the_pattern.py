"""
Print the pattern

You a given a number N. You need to print the pattern for the given value of N.
for N=2 the pattern will be
2 2 1 1
2 1
for N=3 the pattern will be
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Input Format:
The first line of input is the number of testcases T. The T test cases follow. The first line of each test case is an integer N.

Output Format:
For each test case, in a new line, print the required pattern in a singleline .
Note : Instead of printing new line print a "$" without quotes.

Your Task:
Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function printPat which takes one argument 'N' denoting the length of the pattern.

Constraints:
1 <= T <= 20
1 <= N <= 40

Example:
Input
2
2
3
Output
2 2 1 1 $2 1 $
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $
"""


def get_pattern(n):
    pat_out = ""
    for row in range(n, 0, -1):
        row_out = ""
        for num in range(n, 0, -1):
            for seq in range(row, 0, -1):
                row_out += str(num) + " "
        pat_out += row_out + "$"
    return pat_out


if __name__ == '__main__':
    total_inputs = int(input())
    for inp in range(total_inputs):
        inp_num = int(input())
        print(get_pattern(inp_num))
