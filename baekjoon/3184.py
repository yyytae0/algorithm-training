from collections import deque


def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b])
    sh, wo = 0, 0
    visit[a][b] = 1
    if lst[a][b] == 'o':
        sh += 1

    elif lst[a][b] == 'v':
        wo += 1

    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1]]
            n0 = new_v[0]
            n1 = new_v[1]
            if 0 <= n0 <= r-1 and 0 <= n1 <= c-1 and not visit[n0][n1] and lst[n0][n1] != '#':
                q.append(new_v)
                visit[n0][n1] = 1
                if lst[n0][n1] == 'o':
                    sh += 1

                elif lst[n0][n1] == 'v':
                    wo += 1

    return sh, wo


r, c = map(int, input().split())
lst = list(list(input()) for _ in range(r))
visit = [[0 for _ in range(c)] for _ in range(r)]
t_o, t_v = 0, 0
for i in range(r):
    for j in range(c):
        if lst[i][j] != '#' and not visit[i][j]:
            o, v = bfs(i, j)
            if o > v:
                v = 0
            else:
                o = 0
            t_o += o
            t_v += v
print(t_o, t_v)
