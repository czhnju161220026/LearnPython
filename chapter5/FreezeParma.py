from functools import partial
import os

def f(a: int, b: int) -> None:
    print(a, '+', b, '=', a + b)


if __name__ == '__main__':
    freeze_f = partial(f, b=2)
    freeze_f(1)

