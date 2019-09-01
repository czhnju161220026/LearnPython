# encoding=utf-8

class MySeq:
    def __getitem__(self, item):
        return item


if __name__ == '__main__':
    s = MySeq()
    print(s[1])
    print(s[1:4])
    print(s[1:4:2])
    print(s[1, 4, 2])
    print(s[1:4, 9])
    print(s[1:4, 5:7])
    '''
    1
    slice(1, 4, None)
    slice(1, 4, 2)
    (1, 4, 2)
    (slice(1, 4, None), 9)
    (slice(1, 4, None), slice(5, 7, None))
    '''
