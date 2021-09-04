import random

if __name__ == '__main__':
    print("-- 随机选择 --")
    print()

    print("-- 使用 random 模块 --")
    print()

    print("-- 从序列随机抽取一个元素 --")
    values = list(range(1, 7))
    print("values={}".format(values))
    for i in range(1, 6):
        print("随机抽取一个数：{}".format(random.choice(values)))

    random.shuffle(values)
    print("打乱顺序后 values={}".format(values))

    print("-- 生成随机整数 --")
    for i in range(0, 10):
        print("生成 0-10 的随机整数：{}".format(random.randint(0, 10)))

    print("-- 生成 0-1 随机数 --")
    for i in range(0, 10):
        print("随机数：{:.2f}".format(random.random()))
