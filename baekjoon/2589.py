from collections import deque


def bfs(a, b):
    global mx
    q = deque()
    q.append([a, b, 0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] == 'L':
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
    if mx < v[2]:
        mx = v[2]


way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
mx = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'L':
            bfs(i, j)
print(mx)
