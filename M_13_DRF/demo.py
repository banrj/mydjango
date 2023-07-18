from functools import cache


@cache
def factorial(num):

    if num < 2:
        return num

    return num * factorial(num-1)


def main():
    print(factorial(5))
    print(factorial(3))
    print(factorial(7))


if __name__ == '__main__':
    main()
