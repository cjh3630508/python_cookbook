class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

    # Reverse iterator
    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


if __name__ == '__main__':
    print("-- 反向迭代 --")
    print()

    """
    反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
    如果两者都不符合，那你必须先将对象转换为一个列表才行
    """

    print("-- 使用内置的 reversed() --")
    for x in reversed(range(1, 5)):
        print(x)

    print("-- 定义 __reversed__ --")
    print("正向迭代")
    for rr in Countdown(5):
        print(rr)
    print("反向迭代")
    for rr in reversed(Countdown(5)):
        print(rr)
