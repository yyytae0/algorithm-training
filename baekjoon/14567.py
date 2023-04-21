from collections import deque
from sys import stdin


def topology_sort():
    while q:
        v = q.pop()
        for i in lst[v[0]]:
            temp[i] -= 1
            ans[i - 1] = max(v[1] + 1, ans[i-1])
            if not temp[i]:
                q.append([i, v[1]+1])


n, m = map(int, stdin.readline().split())
lst = [[] for _ in range(n+1)]
temp = [0 for _ in range(n+1)]
ans = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    temp[b] += 1
q = deque()
for i in range(1, n+1):
    if not temp[i]:
        q.append([i, 1])
        ans[i-1] = 1
topology_sort()
print(*ans)
