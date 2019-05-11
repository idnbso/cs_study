def factorial(x):
    if x <= 1:
        return 1

    return x * factorial(x - 1)


if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
