from collections import deque


def melt():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if lst[i][j] > 0:
                for dr in [[1,0], [-1,0], [0,1], [0,-1]]:
                    if 0 <= i+dr[0] <= n-1 and 0 <= j+dr[1] <= m-1 and not lst[i+dr[0]][j+dr[1]]:
                        lst[i][j] -= 1
                        if not lst[i][j]:
                            lst[i][j] = -1
                            break


def bfs(a, b):
    way = [[1,0], [-1,0], [0,1], [0,-1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1]]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= m-1 and lst[nv[0]][nv[1]] > 0 and not visit[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1


def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == -1:
                lst[i][j] = 0
            elif lst[i][j]:
                if not visit[i][j]:
                    bfs(i, j)
                    cnt += 1
            if cnt >= 2:
                return True
    return False


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
t = 0
while True:
    t += 1
    melt()
    for i in lst:
        print(*i)
    visit = [[0 for _ in range(m)] for _ in range(n)]
    if check():
        print(t)
        break

