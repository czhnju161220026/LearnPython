import collections

Card = collections.namedtuple('Card', ['rank', 'shape'])


def card_cmp(card):
    rank_value = len(FrenchDeck.shapes) * FrenchDeck.ranks.index(card.rank) + FrenchDeck.shape_value[card.shape]
    return rank_value


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    shapes = ['HEARTS', 'SPADES', 'DIAMONDS', 'CLUBS']
    shape_value = dict(HEARTS=1, SPADES=2, DIAMONDS=3, CLUBS=4);

    def __init__(self):
        self._cards = [Card(rank, shape) for shape in self.shapes for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    


if __name__ == '__main__':
    decks = FrenchDeck()
    for card in sorted(decks, key=card_cmp):
        print(card)

