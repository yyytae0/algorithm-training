from sys import stdin


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.next = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        now = self.head
        for char in string:
            if not now.next[ord(char)-97]:
                now.next[ord(char)-97] = Node(char)
            now = now.next[ord(char)-97]
        now.data = string


def check_color():
    global ans
    now = color.head
    for i in range(na):
        if now.data:
            check_name(i)
        if ans:
            return
        if not now.next[ord(a[i])-97]:
            return
        now = now.next[ord(a[i])-97]


def check_name(idx):
    global ans
    now = name.head
    for i in range(idx, na):
        if not now.next[ord(a[i])-97]:
            return
        now = now.next[ord(a[i])-97]
    if now.data:
        ans = True
    return


n, m = map(int, stdin.readline().split())
color = Trie()
name = Trie()
for i in range(n):
    a = stdin.readline().strip()
    color.insert(a)
for i in range(m):
    a = stdin.readline().strip()
    name.insert(a)
t = int(stdin.readline())
for i in range(t):
    a = stdin.readline().strip()
    na = len(a)
    ans = False
    check_color()
    if ans:
        print("Yes")
    else:
        print("No")
