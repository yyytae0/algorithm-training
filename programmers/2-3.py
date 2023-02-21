from collections import deque


def bfs(a, b, n, m, maps, visit):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    food = int(maps[a][b])
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and maps[nv[0]][nv[1]].isdigit() and not visit[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                food += int(maps[nv[0]][nv[1]])
    return food


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit() and not visit[i][j]:
                d = bfs(i, j, n, m, maps, visit)
                answer.append(d)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
