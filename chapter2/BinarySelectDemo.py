from bisect import bisect, insort

ARRAY = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
CANDIDATES = [0, 2, 5, 8, 14, 25, 31]
ROW_FORMAT = '{0:2d} @ {1:2d}   {2}{0:<2d}'


def demo_sect():
    for candidate in reversed(CANDIDATES):
        position = bisect(ARRAY, candidate)
        offset = '   |' * position
        print(ROW_FORMAT.format(candidate, position, offset))


def demo_insort():
    my_list = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    for candidate in reversed(CANDIDATES):
        insort(my_list, candidate)
        print('%2d -> ' % candidate, my_list)

if __name__ == '__main__':
    print('DEMO:', bisect.__name__)
    print('ARRAY ->   ', '  '.join('%2d' % n for n in ARRAY))
    demo_sect()
    print('DEMO:', insort.__name__)
    demo_insort()
    
