# encoding=utf-8

from collections import namedtuple
from random import shuffle

Card = namedtuple('Card', ['rank', 'suit'])


def set_item(deck, position, value):
    deck.cards[position] = value

class FrenchDeck:
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
    #def __setitem__(self, key, value):
    #    self.cards[key] = value


# Python的思想是忽略对象的真正类型
# 关注对象是否实现了所需的方法，功能和语义
if __name__ == '__main__':
    fd = FrenchDeck()
    print(fd)
    print(fd[1:10])
    print(fd[::4])

    FrenchDeck.__setitem__ = set_item
    try:
        shuffle(fd)
    except TypeError:
        print('Not support')
    print(fd[:5])
