class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def find_max_value(root: Node):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.val


def find_min_value(root: Node):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.val


def find_sum(root: Node):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)


def insert(root: Node, key: int):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    print("Max value:", find_max_value(root))
    print("Min value:", find_min_value(root))
    print("Sum:", find_sum(root))
    print(root)
