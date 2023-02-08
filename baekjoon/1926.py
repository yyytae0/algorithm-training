from collections import deque


def bfs(a, b):
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1]]
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= m-1 and not visit[new_v[0]][new_v[1]] and lst[new_v[0]][new_v[1]]:
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1
                cnt += 1
    return cnt


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
mx = 0
c = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and lst[i][j]:
            dummy = bfs(i, j)
            c += 1
            if dummy > mx:
                mx = dummy

print(c)
print(mx)
