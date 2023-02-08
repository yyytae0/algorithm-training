from collections import deque
from sys import stdin


def bfs(a):
    q = deque()
    q.append(a)
    visit[a] = 1
    cnt = 1
    while q:
        v = q.popleft()
        if lst[v]:
            for i in dct[v]:
                if not visit[i]:
                    visit[i] = 1
                    q.append(i)
                    cnt += 1
    return cnt


n, m = map(int, stdin.readline().split())
dct = dict()
lst = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    if lst[y]:
        dct[y].append(x)

    else:
        dct[y] = [x]
        lst[y] = 1

mx = 0
ans = list()
for i in dct.keys():
    visit = [0 for _ in range(n + 1)]
    dummy = bfs(i)
    if dummy > mx:
        mx = dummy
        ans = [i]

    elif dummy == mx:
        ans.append(i)

ans.sort()
print(*ans)
