from collections import deque


def find():
    for i in range(r):
        for j in range(c):
            if lst[i][j] == 'S':
                return [i, j]


def floud():
    visit = [[0 for _ in range(c)] for _ in range(r)]
    q = deque()
    for i in water:
        q.append([i[0], i[1], 1])
        visit[i[0]][i[1]] = 1
        d[i[0]][i[1]] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < r and 0 <= nv[1] < c and not visit[nv[0]][nv[1]] and 0 <= d[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                d[nv[0]][nv[1]] = nv[2]


def bfs(s):
    visit = [[0 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append([s[0], s[1], 1])
    visit[s[0]][s[1]] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < r and 0 <= nv[1] < c and not visit[nv[0]][nv[1]] and d[nv[0]][nv[1]] != -2:
                if nv[2] < d[nv[0]][nv[1]] or d[nv[0]][nv[1]] == 0:
                    q.append(nv)
                    visit[nv[0]][nv[1]] = 1
                if [nv[0], nv[1]] == t:
                    return nv[2]-1
    return 'KAKTUS'


r, c = map(int, input().split())
lst = list(list(input()) for _ in range(r))
d = [[0 for _ in range(c)] for _ in range(r)]
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
s = find()
t = []
water = []
for i in range(r):
    for j in range(c):
        if lst[i][j] == '*':
            water.append([i, j])
        elif lst[i][j] == 'D':
            d[i][j] = -1
            t = [i, j]
        elif lst[i][j] == 'X':
            d[i][j] = -2
floud()
# for i in d:
#     print(*i)
print(bfs(s))
