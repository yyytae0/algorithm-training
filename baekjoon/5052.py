from sys import stdin


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.next = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        global dummy
        now = self.head
        for char in string:
            if not now.next.get(char):
                now.next[char] = Node(char)
            now = now.next[char]
            if now.data:
                dummy = 1
                return
        now.data = string
        if now.next:
            dummy = 1


t = int(stdin.readline())

for case in range(t):
    n = int(stdin.readline())
    trie = Trie()
    dummy = 0
    for i in range(n):
        a = stdin.readline().strip()
        if dummy:
            continue
        trie.insert(a)
    if dummy:
        print('NO')
    else:
        print('YES')
