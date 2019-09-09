# encoding=utf-8

from collections import namedtuple, MutableSequence
from random import shuffle

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(MutableSequence):
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ([str(i) for i in range(1, 10)] + list('JQKA'))
                      for suit in ['spades', 'diamonds', 'clubs', 'hearts']]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def __repr__(self):
        return str(self.cards)

    # 可以使用猴子补丁动态添加功能
    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def insert(self, index: int, object):
        self.cards.insert(index, object)


#
if __name__ == '__main__':
    fd = FrenchDeck2()
    print(fd)
    print(fd[1:10])
    print(fd[::4])
    try:
        shuffle(fd)
    except TypeError:
        print('Not support')
    print(fd[:5])

    del fd[0:5]
    print(len(fd))
