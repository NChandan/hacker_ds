from collections import defaultdict


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


def _topLeft(root):
    if root.left is None:
        print(root.info, end=" ")
        if root.right is None:
            return
        _topLeft(root.right)
    _topLeft(root.left)
    print(root.info, end=" ")

def _topRight(root):
    # if root is not None:
    print(root.info, end=" ")
    if root.right is None:
        if root.left is None:
            return
        _topRight(root.left)
    _topRight(root.right)


def top_view(root):
    ele = defaultdict(list)
    q = []
    initial_q = (root, 0)
    q.append(initial_q)
    while len(q) != 0:
        cur_q = q[0]
        curr_node = cur_q[0]
        q = q[1:]
        ele[cur_q[1]].append(curr_node.info)
        if curr_node.left is not None:
            q.append((curr_node.left, cur_q[1] - 1))
        if curr_node.right is not None:
            q.append((curr_node.right, cur_q[1] + 1))
    for i in sorted(ele.keys()):
        print(ele[i][0], end=" ")

def level_order(root):
    lvl_dict =defaultdict(list)
    node_list = [(root, 0)]
    while len(node_list):
        curr_node = node_list[0]
        node = curr_node[0]
        lvl = curr_node[1]
        node_list = node_list[1:]
        lvl_dict[lvl].append(str(node.info))
        if node.left is not None:
            node_list.append((node.left, lvl+1))
        if node.right is not None:
            node_list.append((node.right, lvl+1))
    for key in sorted(lvl_dict.keys()):
        print(" ".join(lvl_dict[key]), end=" ")
def topView(root):
    # Write your code here
    q = []
    dic = defaultdict(list)

    q.append((root, 0, 0))  # node, height, distance
    while len(q) != 0:
        cur = q[0]
        cur_node = q[0][0]
        q = q[1:]
        # print (cur_node.info,cur[1],cur[2])
        dic[cur[1]].append(cur_node.info)

        if cur_node.left is not None:
            q.append((cur_node.left, cur[1] - 1))
        if cur_node.right is not None:
            q.append((cur_node.right, cur[1] + 1))

    # print (dic)
    for i in sorted(dic.keys()):
        print(dic[i][0], end=" ")

tree = BinarySearchTree()
t = 116 #int(input())

arr = list(map(int, "37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 "
                    "74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 "
                    "112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 "
                    "116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3".split()))

for i in range(t):
    tree.create(arr[i])

# top_view(tree.root)
level_order(tree.root)