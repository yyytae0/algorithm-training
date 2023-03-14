def dfs(a):
    global ans
    if a == cnt:
        d = unsafe()
        if d < ans:
            ans = d
        return
    for i in cctv[lst[t[a][0]][t[a][1]]]:
        for j in i:
            check(i, t[a][0], t[a][1])
        dfs(a + 1)
        for j in i:
            uncheck(i, t[a][0], t[a][1])


def check(way, i, j):
    for k in way:
        ni, nj = i+k[0], j+k[1]
        while 0 <= ni < n and 0 <= nj < m:
            if lst[ni][nj] <= 0:
                lst[ni][nj] -= 1
            elif lst[ni][nj] == 6:
                break
            ni, nj = ni + k[0], nj + k[1]


def uncheck(way, i, j):
    for k in way:
        ni, nj = i+k[0], j+k[1]
        while 0 <= ni < n and 0 <= nj < m:
            if lst[ni][nj] < 0:
                lst[ni][nj] += 1
            elif lst[ni][nj] == 6:
                break
            ni, nj = ni + k[0], nj + k[1]


def unsafe():
    d = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                d += 1
    return d


cctv = [[], [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]], [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]], [[[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, 1]], [[-1, 0], [0, -1]]],
        [[[1, 0], [-1, 0], [0, 1]], [[1, 0], [-1, 0], [0, -1]], [[1, 0], [0, 1], [0, -1]], [[-1, 0], [0, 1], [0, -1]]], [[[1, 0], [-1, 0], [0, 1], [0, -1]]]]
n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
t = []
cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 5:
            check(cctv[5][0], i, j)
        elif 0 < lst[i][j] < 6:
            t.append([i, j])
            cnt += 1
ans = unsafe()
if t:
    dfs(0)
print(ans)
