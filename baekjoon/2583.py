from collections import deque


def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    ct = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= m-1 and 0 <= new_v[1] <= n-1 and lst[new_v[0]][new_v[1]] and not visit[new_v[0]][new_v[1]]:
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1
                ct += 1

    return ct


m, n, k = map(int, input().split())
lst = [[1 for _ in range(n)] for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            lst[j][i] = 0

cnt = 0
ans = []
for i in range(m):
    for j in range(n):
        if lst[i][j] and not visit[i][j]:
            dummy = bfs(i, j)
            cnt += 1
            ans.append(dummy)

print(cnt)
ans.sort()
print(*ans)
