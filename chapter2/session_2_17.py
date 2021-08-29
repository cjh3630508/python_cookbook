import html

if __name__ == '__main__':
    print("-- 在字符串中处理 html 和 xml --")
    print()

    str = 'Elements are written as "<tag>text</tag>".'
    print("str is")
    print(str)
    print()

    print("-- 替换 <、> 等 为编码实体，使用 html.escape --")
    print(html.escape(str))
    print('取消”引号“号转换')
    print(html.escape(str, quote=False))
    print()

    print("-- 编码实体还原 html.unescape --")
    str = 'Spicy &quot;Jalape&#241;o&quot.'
    print("str is")
    print(str)

    print(html.unescape(str))
