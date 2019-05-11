def fib(term):
    if term == 0:
        return 0

    if term == 1 or term == 2:
        return 1

    return fib(term - 1) + fib(term - 2)


if __name__ == '__main__':
    print(fib(4))  # 3
    print(fib(10))  # 55
    print(fib(28))  # 317811
    print(fib(35))  # 9227465
