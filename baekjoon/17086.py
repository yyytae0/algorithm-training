from collections import deque


def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    q = deque()
    q.append([a, b, 0])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1], v[2]+1]
            n0 = new_v[0]
            n1 = new_v[1]
            if 0 <= n0 <= n-1 and 0 <= n1 <= m-1 and not visit[n0][n1]:
                q.append(new_v)
                visit[n0][n1] = 1
                if lst[n0][n1] == 1:
                    return new_v[2]


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
mx = 0
for i in range(n):
    for j in range(m):
        if not lst[i][j]:
            visit = [[0 for _ in range(m)] for _ in range(n)]
            dummy = bfs(i, j)
            if dummy > mx:
                mx = dummy
print(mx)
