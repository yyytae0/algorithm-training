from sys import stdin
from collections import deque


def bfs(a):
    q = deque()
    q.append(a)
    while q:
        v = q.popleft()
        for i in range(1, n+1):
            if link[v][i] == 1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1


n, m = map(int, stdin.readline().split())
link = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    link[a][b] = 1
    link[b][a] = 1

cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
