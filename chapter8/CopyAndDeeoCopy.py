# encoding=utf-8
from copy import copy, deepcopy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return repr(self.passengers)


if __name__ == '__main__':
    bus1 = Bus(['Alice', 'Bob', 'David', 'Eddie'])
    bus2 = copy(bus1)
    bus3 = deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.pick('Freddy')
    print(bus2)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    print(bus3)
'''
10357296 10358128 14058608
['Alice', 'Bob', 'David', 'Eddie', 'Freddy']
10458416 10458416 10362552
['Alice', 'Bob', 'David', 'Eddie']
'''
