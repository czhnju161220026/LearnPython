
if __name__ == '__main__':
    # [begin, end)
    a = list(range(10))
    print(a[0:5])  # [0, 1, 2, 3, 4]
    print(a[:5])  # [0, 1, 2, 3, 4]
    print(a[5:])  # [5, 6, 7, 8, 9]
    # seq[start:stop:step]
    print(a[::2])  # [0, 2, 4, 6, 8] equivalent to a[0:10:2]
    print(a[::-2])  # [9, 7, 5, 3, 1]
    a[0:5] = [123]
    print(a)
