import re

if __name__ == '__main__':
    print("-- 最短匹配模式 --")
    print("-- 贪婪匹配 * 号 --")
    str = '"abc"def"gh"'
    print("字符串：{}".format(str))
    reg = r'"(.*)"'
    print("贪婪匹配正则：{}".format(reg))
    print("匹配结果：{}".format(re.findall(reg, str)))

    print("\n")
    print("-- 最短匹配， * 后面加 ？ --")
    reg = r'"(.*?)"'
    print("贪婪匹配正则：{}".format(reg))
    print("匹配结果：{}".format(re.findall(reg, str)))
