from sys import stdin


class Node(object):
    def __init__(self, key, data=0):
        self.key = key
        self.data = data
        self.next = {}
        self.me = False


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        now = self.head
        for char in string:
            if not now.next.get(char):
                now.next[char] = Node(char)
                now.data += 1
            now = now.next[char]
        now.me = True


def check(now, cnt):
    global ans
    if now.me:
        ans += cnt
        if now.data == 1:
            cnt += 1
    for i in now.next:
        if now.data == 1:
            check(now.next[i], cnt)
        else:
            check(now.next[i], cnt+1)


while True:
    try:
        n = int(stdin.readline())
    except:
        break
    trie = Trie()
    ans = 0
    for i in range(n):
        a = stdin.readline().strip()
        trie.insert(a)
    dummy = 0
    if trie.head.data == 1:
        dummy = 1
    check(trie.head, dummy)
    print(f'{ans/n:0.2f}')
