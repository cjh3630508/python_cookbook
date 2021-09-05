from collections import deque

if __name__ == '__main__':
    print("-- 迭代器代替 while 无限循环 --")
    print()

    nums = deque(range(0, 10))
    ''' 第一个参数是 可选的 callable 对象，第二个是停止标志 '''
    for num in iter(lambda: nums.pop(), 5):
        print(num, end='\t')
