class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.info, end=" ")

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)

tree = BinarySearchTree()
t = 15 #int(input())

arr = list(map(int, "8 14 3 7 4 5 15 6 13 10 11 2 12 1 9".split()))
print("8 14 3 7 4 5 15 6 13 10 11 2 12 1 9")
for i in range(t):
    tree.create(arr[i])

post_order(tree.root)