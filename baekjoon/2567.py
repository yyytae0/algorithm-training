from collections import deque


def bfs(i, j):
    global ans
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1]]
            if 0 <= nv[0] < 100 and 0 <= nv[1] < 100 and not lst[nv[0]][nv[1]]:
                ans += 1
            elif nv[0] == -1 or nv[0] == 100 or nv[1] == -1 or nv[1] == 100:
                ans += 1

        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < 100 and 0 <= nv[1] < 100 and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1


lst = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            lst[a+i][b+j] = 1

visit = [[0 for _ in range(100)] for _ in range(100)]
ans = 0

for i in range(100):
    for j in range(100):
        if not visit[i][j] and lst[i][j]:
            bfs(i, j)
print(ans)