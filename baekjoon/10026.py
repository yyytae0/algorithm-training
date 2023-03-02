from collections import deque


def bfs0(a, b, t):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit0[a][b] = 1
    q = deque()
    q.append([a, b])
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and lst[nv[0]][nv[1]] == t and not visit0[nv[0]][nv[1]]:
                q.append(nv)
                visit0[nv[0]][nv[1]] = 1
    return 1


def bfs1(a, b, t):
    if t == 'R':
        t_lst = ['R', 'G']
    else:
        t_lst = ['B']
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit1[a][b] = 1
    q = deque()
    q.append([a, b])
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit1[nv[0]][nv[1]]:
                if lst[nv[0]][nv[1]] in t_lst:
                    q.append(nv)
                    visit1[nv[0]][nv[1]] = 1
    return 1


n = int(input())

lst = list(input() for _ in range(n))
visit0 = [[0 for _ in range(n)] for _ in range(n)]
visit1 = [[0 for _ in range(n)] for _ in range(n)]
ans0, ans1 = 0, 0
for i in range(n):
    for j in range(n):
        if not visit0[i][j]:
            ans0 += bfs0(i, j, lst[i][j])
        if not visit1[i][j]:
            if lst[i][j] == 'B':
                ans1 += bfs1(i, j, lst[i][j])
            else:
                ans1 += bfs1(i, j, 'R')
print(ans0, ans1)
