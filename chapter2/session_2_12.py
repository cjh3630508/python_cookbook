import sys
import unicodedata
from collections import ChainMap

if __name__ == '__main__':
    print("-- 审查清理文本字符串 --")
    str = 'pýtĥöñ\fis\tawesome\r\n'
    print("str is [{}]".format(str))

    print("-- 使用 translate --")
    # ord : 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
    # chr : 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # 删除
    }
    print("after translate : [{}]".format(str.translate(remap)))

    print("-- 删除所有和音符 --")
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    normalize_str = unicodedata.normalize('NFD', str)
    new_remap = ChainMap(remap, cmb_chrs)
    print("normalize str [{}]".format(normalize_str))
    print("translate normalize str [{}]".format(normalize_str.translate(new_remap)))
