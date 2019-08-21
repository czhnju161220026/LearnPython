# encoding = utf-8
from datetime import datetime
import time

def clock(func):
    def inner(*args):
        begin = time.time()
        res = func(*args)
        end = time.time()
        elapsed = end - begin
        args_str = ','.join([str(arg) for arg in args])
        print('[%.8fs] %s(%s)->%r' % (elapsed, func.__name__, args_str, res))
        return res

    return inner


@clock
def factorial(n: int) -> int:
    time.sleep(0.0001)
    res = 1
    if n <= 1:
        return res
    else:
        for i in range(1, n + 1):
            res *= i
        return res


def main():
    print('6!=', factorial(6))
    print('10!=', factorial(10))


if __name__ == '__main__':
    main()
    '''
    [15625.00000000ms] factorial(6)->720
    6!= 720
    [15625.00000000ms] factorial(10)->3628800
    10!= 3628800
    '''
