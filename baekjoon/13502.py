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


def dfs(v, now):
    global ans
    if now.data:
        ans += 1
        now.data = 0
    for i in way:
        nv = [v[0]+i[0], v[1]+i[1]]
        if 0 <= nv[0] < 5 and 0 <= nv[1] < 5 and not visit[nv[0]][nv[1]]:
            if now.next.get(lst[nv[0]][nv[1]]):
                visit[nv[0]][nv[1]] = 1
                dfs(nv, now.next[lst[nv[0]][nv[1]]])
                visit[nv[0]][nv[1]] = 1


way = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1]]
lst = list(list(input().split()) for _ in range(5))
visit = [[0 for _ in range(5)] for _ in range(5)]
ans = 0
