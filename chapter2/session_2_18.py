import re

if __name__ == '__main__':
    print("-- 字符串令牌解析 --")
    print()

    str = 'foo = 23 + 42 * 10'
    print("-- 使用 ?P<TOKENNAME>  给一个模式命名 --")
    reg_name = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    reg_num = r'(?P<NUM>\d+)'
    reg_plus = r'(?P<PLUS>\+)'
    reg_times = r'(?P<TIMES>\*)'
    reg_eq = r'(?P<EQ>=)'
    reg_ws = r'(?P<WS>\s+)'
    print("-- 使用 scanner 扫描目标文本 --")
    pat_formula = re.compile('|'.join([reg_name, reg_num, reg_plus, reg_times, reg_eq, reg_ws]))
    scanner = pat_formula.scanner(str)
    for matcher in iter(scanner.match, None):
        print({matcher.lastgroup: matcher.group()})
