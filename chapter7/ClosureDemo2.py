# encoding=utf-8

def make_averager():
    count = 0
    total = 0

    def avg(num: float):
        nonlocal count, total
        count += 1
        total += num
        return total / count

    return avg

def main():
    # closure by class
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

if __name__ == '__main__':
    main()
