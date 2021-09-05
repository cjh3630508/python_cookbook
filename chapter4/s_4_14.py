from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


if __name__ == '__main__':
    print("-- 展开嵌套的序列 --")
    print()

    items = [1, 'a', [3, 4, [5, 6, 7], 8]]
    for x in flatten(items):
        print(x, end='\t')
