if __name__ == '__main__':
    print("-- 转换并同时计算数据 --")
    print("使用生成器表达式可以节省内存，不生成临时数据结构")
    print("计算平方和")
    nums = [1, 2, 3, 4, 5]
    print("1 到 5 的平方和 :", sum(x * x for x in nums))
