# encoding=utf-8
from collections import namedtuple
Student = namedtuple('Student', ['name', 'id'])

if __name__ == '__main__':
    print('Alice loves {} {}, and is {:.2f}m tall'.format('open-source', 'software', 1.7))
    print('Alice is a {3} {2} and {1} {0}'.format('happy', ' smiling', 'blue', 'shark'))
    print('Alice is {attr}'.format(attr='beautiful'))
    print('Alice has {0:4} red {1:16}!'.format(5, "balloons"))
    print('{:*^20s}'.format('Alice'))
    for i in range(3, 13):
        print("{:3d} {:4d} {:5d}".format(i, i * i, i * i * i))
    s = Student(name='Alice', id=123456)
    print('{0.name} has id:{0.id}'.format(s))
