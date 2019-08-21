if __name__ == '__main__':
    s = 'abc哈哈'
    b = s.encode(encoding='utf8')
    print(b)
    print(b.decode(encoding='utf8'))
