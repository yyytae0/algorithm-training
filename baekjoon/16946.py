from collections import deque


def bfs(a, b, c):
    visit[a][b][0] = c
    log = [[a, b]]
    q = deque()
    q.append([a, b])
    cnt = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]][0] and lst[nv[0]][nv[1]] == '0':
                visit[nv[0]][nv[1]][0] = c
                log.append(nv)
                q.append(nv)
                cnt += 1
    for i in log:
        visit[i[0]][i[1]][1] = cnt
    return


n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
dummy = 1
for i in range(n):
    for j in range(m):
        if not visit[i][j][0] and lst[i][j] == '0':
            bfs(i, j, dummy)
            dummy += 1

for i in range(n):
    ans = ""
    for j in range(m):
        if lst[i][j] == "1":
            cnt = 1
            check = []
            for k in way:
                ni, nj = i+k[0], j+k[1]
                if 0 <= ni < n and 0 <= nj < m and lst[ni][nj] == "0" and visit[ni][nj][0] not in check:
                    cnt += visit[ni][nj][1]
                    check.append(visit[ni][nj][0])
            ans += str(cnt%10)
        else:
            ans += "0"
    print(ans)


