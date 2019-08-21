def my_add(a, b):
    return a + b


def f():
    return 'foo', 'bar'


if __name__ == '__main__':
    # demo 1
    students = [('Jack', 123), ('Lucy', 124), ('Tom', 125), ('Lucy', 122)]
    for student in sorted(students):
        print('%r %r' % student)
    # demo 2
    args = (1, 2)
    print(my_add(*args))
    # demo3
    a, b = f()
    print(a, b)
    # demo4
    a, b, *rest = range(10)
    print(a, b, rest)
