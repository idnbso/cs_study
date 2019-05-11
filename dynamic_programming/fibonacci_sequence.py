"""
Preconditions for Dynamic Programming problem solving:
* Overlapping sub-problems
* Optimal substructure

"""


def fib_dp_tabulation(n):
    """
    Bottom Down Approach
    :param n:
    :return:
    """
    if n <= 2: return 1
    #           0  1  2
    fib_nums = [0, 1, 1]
    for i in range(3, n+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    return fib_nums[n]


def fib_dp(inp):
    """
    Top Down Approach
    :param inp:
    :return:
    """
    cache = {1: 1, 2: 1}
    iterations = {'i': 0}

    def fib_less_efficient(n):
        iterations['i'] += 1
        if n in cache:
            return cache[n]

        res = fib(n - 1) + fib(n - 2)
        cache[n] = res
        return res

    def fib(n):
        iterations['i'] += 1

        m1 = cache[n - 1] if (n - 1) in cache else fib(n - 1)
        m2 = cache[n - 2] if (n - 2) in cache else fib(n - 2)

        cache[n - 1] = m1
        cache[n - 2] = m2

        return m1 + m2

    result = fib(inp)
    print(f'iterations: {iterations}')
    print(f'cache: {cache}')
    return result


def fib_rec(n):
    iterations = {'i': 0}

    def fib(n):
        """
        O(2^N)
        Finds the nth fibonacci number.
        :param n: the index of the number, starting from 0
        :return: the nth fibonacci number
        """
        iterations['i'] += 1
        if n <= 2:
            return 1

        return fib(n - 1) + fib(n - 2)

    result = fib(n)
    print(f'iterations: {iterations}')
    return result


if __name__ == '__main__':
    """
    Fibonacci Sequence:
    1 2 3 4 5 6 7  8  9  10
    1 1 2 3 5 8 13 21 34 55
    """
    print(f'{10}th fibonacci: {fib_rec(10)}')
    print(f'{10}th fibonacci: {fib_dp(10)}')
    print(f'{10}th fibonacci: {fib_dp_tabulation(10)}')
