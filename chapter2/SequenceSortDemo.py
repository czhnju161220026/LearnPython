from random import  randint
if __name__ == '__main__':
    a = [randint(0, 100) for i in range(10)]
    print('a=%r, id=%r' % (a, id(a)))
    a = sorted(a, reverse=True)  # return a new list
    print('a=%r, id=%r' % (a, id(a)))

    a = [randint(0, 100) for i in range(10)]
    print('a=%r, id=%r' % (a, id(a)))
    a.sort()  # sort locally
    print('a=%r, id=%r' % (a, id(a)))

    b = ['banana', 'apple', 'orange', 'watermelon', 'berry']
    b.sort(reverse=True)
    print(b)
    b.sort(key=len)
    print(b)
