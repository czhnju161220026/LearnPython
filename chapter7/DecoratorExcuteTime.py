# encoding=utf-8
registry = []

def register(function):
    print('running register(%s)' % function)
    registry.append(function)
    return function

@register
def func1():
    print('running func1()')

@register
def func2():
    print('running func2()')

def func3():
    print('running func3()')

def main():
    print('running main()')
    print('registry->%r' % registry)
    func1()
    func2()
    func3()
v 
if __name__ == '__main__':
    main()
