from sys import setrecursionlimit


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, t):
        now = self.root
        while True:
            if t < now.key:
                if now.left:
                    now = now.left
                else:
                    now.left = Node(t)
                    return
            else:
                if now.right:
                    now = now.right
                else:
                    now.right = Node(t)
                    return


def check(now):
    for i in [now.left, now.right]:
        if i:
            check(i)
    print(now.key)


setrecursionlimit(10**5)
n = int(input())
tree = Tree(n)
while True:
    try:
        n = int(input())
    except:
        break
    tree.insert(n)
check(tree.root)
