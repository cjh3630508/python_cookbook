from collections import deque


class LineHistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    print("-- 带有外部状态的生成器函数 --")
    print()

    with open('../files/s_4_6.txt') as f:
        lines = LineHistory(f)
        for line in lines:
            if 'python' in line:
                # 访问迭代器状态
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
