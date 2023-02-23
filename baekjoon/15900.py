from collections import deque
from sys import stdin


def bfs(a):
    ans = 0
    q = deque()
    q.append([a, 0])
    visit[a] = 1
    while q:
        d = 0
        v = q.popleft()
        for i in lst[v[0]]:
            if not visit[i]:
                q.append([i, v[1] + 1])
                visit[i] = 1
                d = 1
        if not d:
            ans += v[1]
    return ans


n = int(stdin.readline())
lst = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
game = bfs(1)
if game%2:
    print('Yes')
else:
    print('No')
