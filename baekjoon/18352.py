from collections import deque
from sys import stdin


def bfs(a):
    q = deque()
    q.append([a, 0])
    visit[a] = 1
    while q:
        v = q.popleft()
        if v[1] > k:
            break

        if chk[v[0]]:
            for i in lst[v[0]]:
                if not visit[i]:
                    q.append([i, v[1] + 1])
                    visit[i] = 1
                    if dummy[v[1] + 1]:
                        dct[v[1] + 1].append(i)

                    else:
                        dct[v[1] + 1] = [i]
                        dummy[v[1] + 1] = 1


n, m, k, x = map(int, stdin.readline().split())
visit = [0 for _ in range(n+1)]
dummy = [0 for _ in range(n+1)]
chk = [0 for _ in range(n+1)]
lst = dict()
dct = dict()
for _ in range(m):
    dx, dy = map(int, stdin.readline().split())
    if chk[dx]:
        lst[dx].append(dy)

    else:
        lst[dx] = [dy]
        chk[dx] = 1
bfs(x)
if dummy[k]:
    dct[k].sort()
    for i in dct[k]:
        print(i)

else:
    print(-1)
