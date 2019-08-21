# encoding=utf-8

class Averager:
    def __init__(self):
        self.data = []

    def __call__(self, num):
        self.data.append(num)
        total = sum(self.data)
        return total / len(self.data)


def make_averager():
    data = []

    def avg(num: float):
        data.append(num)
        return sum(data) / len(data)

    return avg


def main():
    # closure by class
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    # closure by advanced function
    avg1 = make_averager()
    print(avg1(10))
    print(avg1(11))
    print(avg1(12))
    # every function object bind with a free variable
    avg2 = make_averager()
    print(avg2(135))
    print(avg2(136))
    print(avg2(137))
    '''
    10.0
    10.5
    11.0
    10.0
    10.5
    11.0
    135.0
    135.5
    136.0
    '''


if __name__ == '__main__':
    main()
