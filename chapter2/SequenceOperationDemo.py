if __name__ == '__main__':
    a = [1] * 5
    b = [2] * 2
    print(a + b)
    print('abcd'*4)

    my_list = [[]]  * 3 # Three references point to the same object
    my_list[0].append(1)
    print(my_list)

    my_list = [[] for i in range(3)]
    my_list[0].append(1)
    print(my_list)



