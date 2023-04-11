class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.next = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, folders):
        now = self.head
        for folder in folders:
            if not now.next.get(folder):
                now.next[folder] = Node(folder)
            now = now.next[folder]


def check(now, dummy):
    for folder in sorted(now.next):
        print(dummy + folder)
        check(now.next[folder], ' '+dummy)


n = int(input())
trie = Trie()
for i in range(n):
    lst = list(input().split(sep="\\"))
    trie.insert(lst)
check(trie.head, '')
