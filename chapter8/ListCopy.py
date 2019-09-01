# encoding=utf-8

if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = list(l1)
    print(l2, id(l2))
    l3 = l1[:]
    print(l3, id(l3))
    l4 = [1, 2, 3, [4, 5, 6]]
    l5 = list(l4)  # shallow copy
    l5[3].append(7)
    print(l4)
