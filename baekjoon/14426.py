from sys import stdin


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        for char in string:
            if not current_node.children.get(char):
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def check(self, string):
        current_node = self.head
        for char in string:
            if not current_node.children.get(char):
                return False
            current_node = current_node.children[char]
        return True


n, m = map(int, stdin.readline().split())
trie = Trie()
for i in range(n):
    trie.insert(stdin.readline().strip())
ans = 0
for i in range(m):
    if trie.check(stdin.readline().strip()):
        ans += 1
print(ans)
