from collections import deque


def bfs(a, b, h):
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1 and not visit[new_v[0]][new_v[1]] and lst[new_v[0]][new_v[1]] > h:
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
mx = 0
for water in range(100):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] > water and visit[i][j] == 0:
                bfs(i, j, water)
                cnt += 1

    if cnt > mx:
        mx = cnt

    if cnt == 0:
        break

print(mx)
