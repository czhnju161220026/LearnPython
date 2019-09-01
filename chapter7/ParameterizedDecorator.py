import time
import math
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args})->{result}'

def clock(fmt=DEFAULT_FMT): #factory of decorator
    def decorate(func):
        def clocked_func(*_args):
            t0 = time.time()
            result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ','.join(str(item) for item in _args)
            print(fmt.format(**locals()))
            return result
        return clocked_func
    return decorate  # generate a decorator


@clock()
def my_sleep(s:float):
    time.sleep(s)

@clock(fmt='{elapsed:.4f} result={result}')
def factorial(n:int):
    return math.factorial(n)

def main():
    my_sleep(0.1)
    my_sleep(0.2)
    factorial(15)
if __name__ == '__main__':
    main()



