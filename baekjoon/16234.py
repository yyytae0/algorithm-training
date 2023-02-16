from collections import deque


def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    ans = lst[a][b]
    cnt = 1
    while q:
        v = q.popleft()
        hv = lst[v[0]][v[1]]
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1]]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= n-1 and not visit[nv[0]][nv[1]]:
                hnv = lst[nv[0]][nv[1]]
                if mn <= abs(hv-hnv) <= mx:
                    q.append(nv)
                    cnt += 1
                    visit[nv[0]][nv[1]] = 1
                    ans += hnv
    return ans, cnt


n, mn, mx = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
t = -1
while True:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dummy = 0
    t += 1
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                ans, cnt = bfs(i, j)
                if cnt == 1:
                    visit[i][j] = 2
                    dummy += 1
                else:
                    for ni in range(n):
                        for nj in range(n):
                            if visit[ni][nj] == 1:
                                visit[ni][nj] = 2
                                lst[ni][nj] = ans//cnt
    # print(lst)
    if dummy == n*n:
        break

print(t)
