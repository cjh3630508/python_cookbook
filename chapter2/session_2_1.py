import re

if __name__ == '__main__':
    print("-- 使用多个界定符风格字符串 --")
    # 匹配到的分隔符两边的实体都会返回，所有最后一个元素是空白
    print("正则分割")
    line = 'asdf fjdk; afed, fjek,asdf, foo '
    print("原始字符串")
    print(line)
    print(re.split(r'[;,\s]\s*', line))
    print("括号分组，分组也会出现在结果")
    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)
    print("分离分组数据")
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(''.join(v + d for v, d in zip(values, delimiters)))
    print("使用分组，但是不保留分组结果 ： (?:...)")
    print(re.split(r'(?:,|;|\s)\s*', line))
