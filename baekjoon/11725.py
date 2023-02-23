from collections import deque
from sys import stdin, stdout


def bfs(a):
    q = deque()
    q.append(a)
    visit[a] = 1
    while q:
        v = q.popleft()
        for i in lst[v]:
            if not visit[i]:
                ans[i-2] = v
                q.append(i)
                visit[i] = 1


n = int(stdin.readline())
lst = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
ans = [0 for _ in range(n-1)]
for i in range(n-1):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
bfs(1)
for i in ans:
    stdout.write(str(i)+'\n')

