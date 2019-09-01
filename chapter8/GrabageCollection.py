# encodng=utf-8
import weakref

def bye():
    print('Gone with wind...')

if __name__ == '__main__':
    s1 = {1,2,3}
    s2 = s1
    ender =weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = [1,2,3]
    print(ender.alive)
