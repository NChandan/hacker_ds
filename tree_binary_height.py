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


def height(root, curr=0):
    if root is None:
        return curr
    curr += 1
    max_left = height(root.left, curr)
    max_right = height(root.right, curr)
    print(max_left, max_right)
    return max_left if max_left > max_right else max_right



tree = BinarySearchTree()
t = 7

arr = list(map(int, "3 5 2 1 4 6 7".split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
