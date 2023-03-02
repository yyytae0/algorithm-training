from collections import deque


def bfs():
    way = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+i[2]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and 0 <= nv[2] < h and not visit[nv[2]][nv[0]][nv[1]] and lst[nv[2]][nv[0]][nv[1]] != -1:
                q.append(nv)
                visit[nv[2]][nv[0]][nv[1]] = 1
                lst[nv[2]][nv[0]][nv[1]] = lst[v[2]][v[0]][v[1]] + 1
    return


def check():
    mx = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if lst[k][i][j] > mx:
                    mx = lst[k][i][j]
                if lst[k][i][j] == 0:
                    return -1
    return mx-1


m, n, h = map(int, input().split())
lst = list(list(list(map(int, input().split())) for _ in range(n)) for _ in range(h))
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if lst[k][i][j] == 1:
                q.append([i, j, k])
                visit[k][i][j] = 1
bfs()
print(check())
