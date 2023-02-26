from collections import deque


def check(a, b):
    visit = [0 for _ in range(n+1)]
    q = deque()
    q.append([a, 0])
    visit[a] = 1
    while q:
        v = q.popleft()
        for i in range(1, n+1):
            if not visit[i] and lst[v[0]][i]:
                q.append([i, v[1] + lst[v[0]][i]])
                visit[i] = 1
                if i == b:
                    return v[1] + lst[v[0]][i]


n, m = map(int, input().split())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c
for i in range(m):
    a, b = map(int, input().split())
    print(check(a, b))
