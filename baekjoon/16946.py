from collections import deque


def bfs(a, b):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[a][b] = 1
    q = deque()
    q.append([a, b])
    cnt = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] == '0':
                visit[nv[0]][nv[1]] = 1
                q.append(nv)
                cnt += 1
    return cnt


n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(n):
    ans = ""
    for j in range(m):
        if lst[i][j] == '1':
            ans += str(bfs(i, j))
        else:
            ans += "0"
    print(ans)

