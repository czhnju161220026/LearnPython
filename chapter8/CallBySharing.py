# encoding=utf-8
# Function may modify mutable objects
def f(a, b):
    a += b
    return a


if __name__ == '__main__':
    x, y = 1, 2
    print(f(x, y), x, y)
    x = [1, 2]
    y = [3, 4]
    print(f(x, y), x, y)
    x = (1, 2)
    y = (3, 4)
    print(f(x, y), x, y)
'''
3 1 2
[1, 2, 3, 4] [1, 2, 3, 4] [3, 4]
(1, 2, 3, 4) (1, 2) (3, 4)
'''
