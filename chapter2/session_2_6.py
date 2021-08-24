import re

if __name__ == '__main__':
    print("-- 字符串忽略大小写的搜索和替换 --")
    print("-- 使用 re 模块时，提供 re.IGNORECASE 标志参数 --")
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print("text is {}\nfind python".format(text))
    print(re.findall('python', text, flags=re.IGNORECASE))
    print("替换 python 为 java")
    print(re.sub("python", "java", text, flags=re.IGNORECASE))
