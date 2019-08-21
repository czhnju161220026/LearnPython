# encoding=utf-8
def decorator(f):
    print('decorator function')
    return f

@decorator
def target():
    print('target function')

if __name__ == '__main__':
    target()
