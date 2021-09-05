import itertools


def count(n):
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == '__main__':
    print("-- 迭代器切片 --")
    print()

    c = count(30)
    for x in itertools.islice(c, 10, 15):
        print(x, end="\t")
