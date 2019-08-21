from functools import reduce # reduce is not a built-in function in python3
from operator import add
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(5))
    print(factorial.__doc__)
    print(type(factorial)) # instance of class function
    fac = factorial
    print(fac(6))
    print(list(map(fac, range(8))))
    print(list(map(fac, filter(lambda x: x%2, range(8))))) # factorial of odd numbers in range(8)
    print(all([1,1,1,1,1]))
    print(any([1,0,0,0,0]))
    print(reduce(add, range(1,100)))
