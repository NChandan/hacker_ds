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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    # if v1 < root.info < v2 or v1 >= root.data > v2:
    #     return root

    while root:
        info = root.info
        if v1 < info < v2 or v1 > info > v2 or info == v1 or info == v2:
            return root
        if info > v1 and info > v2:
            root = root.left
        if info < v1 and info < v2:
            root = root.right
        # if info
    return root
    ...


# Enter your code here

tree = BinarySearchTree()
t = 6

arr = list(map(int, "2 1 3 4 5 6".split()))

for i in range(t):
    tree.create(arr[i])

# v = list(map(int, input().split()))

ans = lca(tree.root, 4, 6)
print(ans.info)
