import re
from collections import defaultdict
from random import randint

WORD_RE = re.compile(r'[a-zA-Z]+')


def method1():
    index = {}
    with open('words.txt', mode='r', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # bad implement
                occurrences = index.get(word, [])  # if word doesn't exist, return an empty list.
                occurrences.append(location)
                index[word] = occurrences
    for word in sorted(index.keys(), key=str.upper):
        print(word, index[word])


def method2():
    index = {}
    with open('words.txt', mode='r', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # good implement
                index.setdefault(word, []).append(location)
    for word in sorted(index.keys(), key=str.upper):
        print(word, index[word])


def method3():
    index = defaultdict(list)  # the constructor of the default value
    with open('words.txt', mode='r', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # better implement
                index[word].append(location)
    for word in sorted(index.keys(), key=str.upper):
        print(word, index[word])


# another example
def method4():
    index = defaultdict(int) # return zero default
    for _ in range(100):
        val = randint(0,10)
        index[val] += 1
    for val in sorted(index.keys()):
        print(val, index[val])

def method5():
    index = {}
    for _ in range(100):
        val = randint(0,10)
        times = index.get(val, 0)
        times += 1
        index[val] = times
    for val in sorted(index.keys()):
        print(val, index[val])


if __name__ == '__main__':
    method5()
