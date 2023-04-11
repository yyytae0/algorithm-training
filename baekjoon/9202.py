from sys import stdin
from collections import deque


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


def bfs(a, b, now):
    q = deque()
    visit = [0 for _ in range(16)]
    q.append([a, b, now, visit])
    while q:
        v = q.popleft()
        for i in way:
            new_visit = visit[:]
            nv = [v[0]+i[0], v[1]+i[1], v[2], new_visit]
            if 0 <= nv[0] < 4 and 0 <= nv[1] < 4:
                pass


def check(visit, trie):
    for i in range(4):
        for j in range(4):
            d = 4*i+j
            now = trie.head
            if not visit[d] and now.next.get(lst[i][j]):
                bfs(i, j, now.next[lst[i][j]])


way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = int(stdin.readline())
for i in range(n):
    a = stdin.readline().strip()

m = int(stdin.readline())
for i in range(m):
    lst = list(list(stdin.readline().strip()) for _ in range(4))
