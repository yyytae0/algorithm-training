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
        for char in string:
            if not now.next.get(char):
                now.next[char] = Node(char)
            now = now.next[char]
        now.data = 1


def check(j, now):
    for i in range(j+1, na):
        if now.data:
            return True
        if not now.next.get(a[i]):
            return False
        now = now.next[a[i]]
    if now.data:
        return True


n = int(input())
trie = Trie()
for i in range(n):
    a = input()
    trie.insert(a)

m = int(input())
for i in range(m):
    a = input()
    na = len(a)

    for j in range(na):
        now = trie.head
        if now.next.get(a[j]):
            if check(j, now.next[a[j]]):
                print("YES")
                break
    else:
        print("NO")
