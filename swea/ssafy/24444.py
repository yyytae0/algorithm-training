from collections import deque
from sys import stdin, stdout

def bfs():
    cnt = 1
    q = deque()
    q.append(r)
    visit[r] = cnt
    cnt += 1
    while q:
        v = q.popleft()
        for i in lst[v]:
            if not visit[i]:
                visit[i] = cnt
                cnt += 1
                q.append(i)


n, m, r = map(int, stdin.readline().split())
lst = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
for i in range(1, n+1):
    lst[i].sort()
bfs()
for i in range(1, n+1):
    stdout.write(str(visit[i])+'\n')
