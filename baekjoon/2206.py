from collections import deque


def bfs():
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q.append([0, 0, 1])
    visit[0][0] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] != 1:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if [nv[0], nv[1]] == [n-1, m-1]:
                    return nv[2]
    return 0


n, m = map(int, input().split())
lst = list(list(map(int, input())) for _ in range(n))
wall = []
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            wall.append([i, j])

mn = 10**6
dummy = 0
for i in wall:
    lst[i[0]][i[1]] = 0
    d = bfs()
    if d:
        if d < mn:
            mn = d
    lst[i[0]][i[1]] = 1

if mn == 10**6:
    print(-1)
else:
    print(mn)