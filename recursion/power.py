def power(x, p):
    if p == 0:
        return 1

    return x * power(x, p - 1)


if __name__ == '__main__':
    print(power(2, 0))
    print(power(2, 1))
    print(power(2, 2))
    print(power(2, 3))
    print(power(2, 5))
