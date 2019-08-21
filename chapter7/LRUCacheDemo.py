# encoding = utf-8
from chapter7.DecoratorDemo import clock
from functools import lru_cache


def fib(n: int) -> int:
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


@lru_cache()  # can be used to optimize recursion
def fib_with_cache(n: int) -> int:
    return 1 if n <= 2 else fib_with_cache(n - 1) + fib_with_cache(n - 2)


@clock
def wrapper1():
    print(fib(20))


@clock
def wrapper2():
    print(fib_with_cache(20))


if __name__ == '__main__':
    wrapper1()
    wrapper2()
    '''
    6765
    [0.01562548s] wrapper1()->None
    6765
    [0.00000000s] wrapper2()->None
    '''
