import heapq

if __name__ == '__main__':
    print("-- 顺序迭代合并后的排序迭代对象 --")
    print()

    a = range(0, 10, 2)
    b = range(1, 10, 2)
    for c in heapq.merge(a, b):
        print(c, end="\t")
