import os
import textwrap

if __name__ == '__main__':
    print("-- 指定列宽格式化字符串 --")
    print()

    str = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, " \
          "don't look around the eyes, look into my eyes, you're under."
    print("str is \n{}".format(str))
    print()

    columns = 70

    print("-- 使用 textwrap --")
    print(textwrap.fill(str, columns))
    print()

    print("-- textwrap initial_indent 首行缩进 --")
    print(textwrap.fill(str, columns, initial_indent="\t"))
    print()

    print("-- textwrap subsequent_indent 首行外缩进 --")
    print(textwrap.fill(str, columns, initial_indent="\t\t", subsequent_indent="\t"))
    print()
