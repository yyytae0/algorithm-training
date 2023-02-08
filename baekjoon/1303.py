from collections import deque


def bfs(a, b, c):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1]]
            if 0 <= new_v[0] <= m-1 and 0 <= new_v[1] <= n-1 and not visit[new_v[0]][new_v[1]] and lst[new_v[0]][new_v[1]] == c:
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1
                cnt += 1

    return cnt


n, m = map(int, input().split())
lst = list(list(input()) for _ in range(m))
visit = [[0 for _ in range(n)] for _ in range(m)]
total_w = 0
for i in range(m):
    for j in range(n):
        if lst[i][j] == 'W' and not visit[i][j]:
            sol = bfs(i, j, 'W')
            total_w += sol**2

visit = [[0 for _ in range(n)] for _ in range(m)]
total_b = 0
for i in range(m):
    for j in range(n):
        if lst[i][j] == 'B' and not visit[i][j]:
            sol = bfs(i, j, 'B')
            total_b += sol**2

print(total_w, total_b)