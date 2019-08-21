if __name__ == '__main__':
    bs = bytes('abc哈哈', encoding='utf8')
    print(bs)
    print(bs[0])
    print(bs[:1]) # slice of bytes is bytes
    ba = bytearray(bs)
    print(ba)
    print(ba[0])
    print(ba[:2]) # slice of bytearray is bytearray
