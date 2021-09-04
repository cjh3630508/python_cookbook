if __name__ == '__main__':
    print("-- 字节到大整数的打包与解包 --")
    print()

    print("-- int.from_bytes --")
    bytes = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print("bytes={}".format(bytes))
    print('小端={}'.format(int.from_bytes(bytes, 'little')))
    print('大端={}'.format(int.from_bytes(bytes, 'big')))
    print()

    big_num = 94522842520747284487117727783387188
    print("-- num.to_bytes --")
    print('小端={}'.format(big_num.to_bytes(16, 'little')))
    print('大端={}'.format(big_num.to_bytes(16, 'big')))
