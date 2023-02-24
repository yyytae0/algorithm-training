from collections import deque
from sys import stdin


def bfs():
    q = deque()
    q.append([0, 0])
    visit[0] = 1
    cnt = lst[0]
    while q:
        v = q.popleft()
        for i in dct[v[0]]:
            if not visit[i]:
                q.append([i, v[1]+1])
                visit[i] = 1
                if v[1]+1 > k:
                    return cnt
                cnt += lst[i]
    return cnt


n, k = map(int, stdin.readline().split())
dct = dict()
visit = [0 for _ in range(n)]
for i in range(n):
    dct[i] = []
for i in range(n-1):
    p, c = map(int, stdin.readline().split())
    dct[p].append(c)
lst = list(map(int, stdin.readline().split()))
print(bfs())
