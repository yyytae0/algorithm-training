class Node(object):
    def __init__(self, key, data=0):
        self.key = key
        self.data = data
        self.next = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        now = self.head
        dummy = 1
        for char in string:
            if dummy:
                print(char, end='')
            if not now.next.get(char):
                dummy = 0
                now.next[char] = Node(char)
            now = now.next[char]
        now.data += 1
        if dummy:
            if now.data > 1:
                print(str(now.data), end='')
        print()


n = int(input())
trie = Trie()
for i in range(n):
    a = input()
    trie.insert(a)
