from collections import deque


def start(n, m, maps):
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                return bfs1(i, j, n, m, maps)


def bfs1(a, b, n, m, maps):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([a, b, 0])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= m-1 and not visit[nv[0]][nv[1]] and maps[nv[0]][nv[1]] != 'X':
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if maps[nv[0]][nv[1]] == 'L':
                    return bfs2(nv[0], nv[1], v[2], n, m, maps)
    return -1


def bfs2(a, b, c, n, m, maps):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([a, b, 0])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1], v[2] + 1]
            if 0 <= nv[0] <= n - 1 and 0 <= nv[1] <= m - 1 and not visit[nv[0]][nv[1]] and maps[nv[0]][nv[1]] != 'X':
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if maps[nv[0]][nv[1]] == 'E':
                    return c + v[2] + 2
    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = start(n, m, maps)
    return answer