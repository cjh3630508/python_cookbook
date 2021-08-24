from collections import ChainMap

if __name__ == '__main__':
    print("-- 合并多个字典或映射 --")
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    print("-- 使用 ChainMap --")
    print("-- 合并后重复建保留第一个--")
    c = ChainMap(a, b)
    print("x={},y={},z={}".format(c['x'], c['y'], c['z']))
    print("对字典的操作会影响第一个字典")
    print("修改 c.z，a.z 更新，b.z 不变")
    c['z'] = 5
    print('a.z={},b.z={},c.z={}'.format(a['z'], b['z'], c['z']))
    print("新增元素，出现在第一个集合")
    c['w'] = 4
    print("a :", a)
    print("b :", b)
    print("c :", c)
    print("删除 z，删除了 a.z")
    del c['z']
    print("a :", a)
    print("b :", b)
    print("c :", c)

