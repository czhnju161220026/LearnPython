# namedtuple is used to defination a class without method
from collections import namedtuple

Student = namedtuple('Student', 'name id') # equivalent to namedtuple('Student', ['name', 'id'])

if __name__ == '__main__':
    s1 = Student(name='Jack', id=1)
    s2 = Student(name='Tom', id=2)
    print(s1) #namedtuple has __repr__
    print(s2)
    #fields
    print(Student._fields)
    # make
    s3 = Student._make(['Lucy', 3])
    print(s3)
    for k,v in s3._asdict().items():
        print('%r : %r' % (k, v))
