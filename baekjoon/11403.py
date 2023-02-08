from collections import deque


def bfs(a):
    q = deque()
    q.append(a)
    while q:
        v = q.popleft()
        for i in range(n):
            if lst[v][i] == 1 and visit[v][i] == 0:
                q.append(i)
                ans[a][i] = 1
                visit[v][i] = 1


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    bfs(i)

for i in ans:
    print(*i)
