def find_min(x):
    while x.left is not None:
        x = x.left
    return x


def next_large(x):
    if x.right is not None:
        return find_min(x.right)
    else:
        y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


class BSTnode(object):
    def __init__(self, parent, t):
        self.key = t
        self.parent = parent
        self.left = None
        self.right = None

    # 要求结点之间的间隔为大于等于3
    def insert(self, t):
        if abs(t-self.key) < 3:
            print("Insert error!")
            return
        if t < self.key:
            if self.left is None:
                self.left = BSTnode(self, t)
                return self.left
            else:
                return self.left.insert(t)
        else:
            if self.right is None:
                self.right = BSTnode(self, t)
                return self.right
            else:
                return self.right.insert(t)


class BST(object):
    def __init__(self):
        self.root = None


if __name__ == '__main__':
    A = [46, 39, 49, 44, 51]

