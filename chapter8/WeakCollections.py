# encoding=utf-8
import weakref


class Cheese:

    def __init__(self, kind: str):
        self.kind = kind

    def __repr__(self):
        return 'Cheese: %s' % self.kind


if __name__ == '__main__':
    stock = weakref.WeakValueDictionary() # remove object without reference automatically
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))


