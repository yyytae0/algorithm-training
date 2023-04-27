from collections import deque


def island(a, b, cnt):
    visit[a][b] = 1
    lst[a][b] = cnt
    q = deque()
    q.append([a, b])
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] == 1:
                lst[nv[0]][nv[1]] = cnt
                visit[nv[0]][nv[1]] = 1
                q.append(nv)


def check(a, b, cnt):
    global mx
    q = deque()
    vi = [[0 for _ in range(n)] for _ in range(n)]
    q.append([a, b, 0])
    vi[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and not vi[nv[0]][nv[1]]:
                vi[nv[0]][nv[1]] = 1
                if not lst[nv[0]][nv[1]]:
                    q.append(nv)
                elif lst[nv[0]][nv[1]] == cnt:
                    nv[2] = 0
                    q.append(nv)
                elif nv[2] < mx:
                    mx = nv[2]


way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
visit = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
islands = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1 and not visit[i][j]:
            cnt += 1
            islands.append([i, j, cnt])
            island(i, j, cnt)
mx = 200
for i in islands:
    check(i[0], i[1], i[2])
print(mx-1)
