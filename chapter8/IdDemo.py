# encoding=utf

if __name__ == '__main__':
    charles={'name':'Charles', 'born':1812}
    lewis = charles # Bind to the same object
    print(id(charles), id(lewis))
    lewis['name'] = 'Lewis'
    print(charles)
    print(lewis is charles) #compare id
    a = [1,2,3]
    b = [1,2,3]
    print(a == b)
    print(a is b)
    '''
    5728320 5728320
    {'name': 'Lewis', 'born': 1812}
    True
    True
    False
    '''
