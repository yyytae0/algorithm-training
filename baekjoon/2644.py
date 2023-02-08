from collections import deque


def bfs(a, b):
    q = deque()
    q.append([a, 0])
    while q:
        v = q.popleft()
        for i in range(n+1):
            if lst[v[0]][i] == 1 and visit[v[0]][i] == 0:
                q.append([i, v[1]+1])
                visit[v[0]][i] = 1
                if i == b:
                    return v[1]+1

    return -1


n = int(input())
a, b = map(int, input().split())
ip = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(ip):
    x, y = map(int, input().split())
    lst[x][y] = 1
    lst[y][x] = 1

print(bfs(a, b))
