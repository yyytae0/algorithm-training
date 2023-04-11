class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.next = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, foods):
        now = self.head
        for food in foods:
            if not now.next.get(food):
                now.next[food] = Node(food)
            now = now.next[food]


def check(now, dummy):
    for food in sorted(now.next):
        print(dummy + food)
        check(now.next[food], dummy+'--')


n = int(input())
trie = Trie()
for i in range(n):
    lst = list(input().split())
    trie.insert(lst[1:])
check(trie.head, '')
