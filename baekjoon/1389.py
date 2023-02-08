from collections import deque


def bfs(a):
    q = deque()
    q.append([a, 0])
    dummy = 0
    while q:
        v = q.popleft()
        for i in range(n+1):
            if lst[v[0]][i] and not visit[i]:
                q.append([i, v[1]+1])
                visit[i] = 1
                dummy = dummy + v[1] + 1

    return dummy


n, m = map(int, input().split())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    lst[x][y] = 1
    lst[y][x] = 1

mn = 10000
ans = n
for i in range(1, n+1):
    visit = [0 for _ in range(n + 1)]
    d = bfs(i)
    if d < mn:
        ans = i
        mn = d

    elif d == mn:
        if i < ans:
            ans = i

print(ans)
