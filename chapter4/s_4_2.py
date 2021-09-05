class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, child_node):
        self.children.append(child_node)

    def __iter__(self):
        return iter(self.children)


if __name__ == '__main__':
    print("-- 代理迭代 --")
    print()

    print("-- __iter__() 方法，将迭代代理到容器内部的对象上 --")
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    print("遍历子节点")
    for child in root:
        print(child)
