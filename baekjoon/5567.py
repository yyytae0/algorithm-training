from collections import deque
from sys import stdin


def bfs():
    q = deque()
    q.append([1, 0])
    visit[1] = 1
    cnt = 0
    while q:
        v = q.popleft()
        if v[1] > 2:
            break
        for i in range(1, n+1):
            if lst[v[0]][i] and not visit[i]:
                q.append([i, v[1]+1])
                visit[i] = 1
                if v[1]+1 <= 2:
                    cnt += 1

    return cnt


n = int(stdin.readline())
m = int(stdin.readline())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    x, y = map(int, stdin.readline().split())
    lst[x][y] = 1
    lst[y][x] = 1

print(bfs())
