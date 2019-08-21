
if __name__ == '__main__':
    a = dict(one=1, two=2, three=3);
    print(a)
    b = {'one':1, 'two':2, 'three':3};
    print(b)
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    print(c)
    d = dict([('one',1), ('two',2), ('three',3)])
    print(d)

    for k in a.keys():
        print(k, a[k])
