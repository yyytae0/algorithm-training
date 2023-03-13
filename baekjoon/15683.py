from collections import deque


def dfs(a):
    for i in cctv[lst[t[a][0]][t[a][1]]]:
        for j in i:
            check(i, a[0], a[1])
            dfs(a + 1)


def check(way, i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    while q:
        v = q.popleft()
        for k in way:
            nv = [v[0]+k[0], v[1]+k[1]]


cctv = [[], [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]], [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]], [[[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, 1]], [[-1, 0], [0, -1]]],
        [[[1, 0], [-1, 0], [0, 1]], [[1, 0], [-1, 0], [0, -1]], [[1, 0], [0, 1], [0, -1]], [[-1, 0], [0, 1], [0, -1]]], [[[1, 0], [-1, 0], [0, 1], [0, -1]]]]
n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
t = []
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            t.append([i, j])
