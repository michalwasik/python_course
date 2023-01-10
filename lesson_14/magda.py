def get_fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def get_fib_rec(n: int) -> int:
    if n in {0, 1}:
        return n
    return get_fib_rec(n - 1) + get_fib_rec(n - 2)


if __name__ == '__main__':
    import sys
    arg = sys.argv[1]
    print(get_fib(int(arg)))
