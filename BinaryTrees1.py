from importlib.machinery import SourcelessFileLoader


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(4)

# print(root)
# print(root.val, root.left, root.right)

# root.left = Node(2)
# root.right = Node(10)
# print(root)
# print(root.val, root.left, root.right)

class BST:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, value):
        if value < self.val:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.add(value)
        return self



root = BST(5)
root.add(4)
root.add(10)
print(root.left.val)
print(root.right.val)