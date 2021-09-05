class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def depth_first(self):
        yield self
        for child in self:
            yield from child.depth_first()


if __name__ == '__main__':
    print("-- 实现迭代器协议 --")
    print()

    print("深度优先遍历")
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for node in root.depth_first():
        print(node)

