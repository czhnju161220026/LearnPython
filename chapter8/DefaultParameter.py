# encoding=utf-8
# Do not use mutable object as default parameter

class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return repr(self.passengers)


if __name__ == '__main__':
    bus1 = HauntedBus()
    bus2 = HauntedBus()
    bus1.pick('Alice')
    bus2.pick('Bob')
    print(bus1, bus2)
    print(bus1.passengers is bus2.passengers)
    
