# set can be used to remove repeated elements.
def method1():
    a = ['egg', 'banana', 'apple', 'egg', 'banana']
    a = list(set(a))
    print(a)


# set operation
def method2():
    # create set
    #a = set(['egg', 'banana', 'apple', 'orange', 'pie'])
    #b = set(['banana', 'apple', 'cake', 'coffee'])
    a = {'egg', 'banana', 'apple', 'orange', 'pie'}
    b = {'banana', 'apple', 'cake', 'coffee'}
    print('a-b:', a - b)
    print('a|b:', a | b)
    print('a&b:', a & b)
    print('a^b:', a ^ b)


if __name__ == '__main__':
    method1()
    method2()
