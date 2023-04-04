from collections import deque

def dfs(a, b):
    if a == n-1 and b == n-1:
        return

    for i in way:
        na = a+i[0]
        nb = b+i[1]
        if 0<=na<n and 0<=nb<n:
            h = abs(lst[na][nb] - lst[a][b])
            if dp[na][nb] > dp[a][b] + 1 + h:
                dp[na][nb] = dp[a][b] + 1 + h
                dfs(na, nb)


def stack():
    q = deque()
    q.append([0, 0])
    while q:
        v = q.pop()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0<=nv[0]<n and 0<=nv[1]<n:
                h = abs(lst[nv[0]][nv[1]]-lst[v[0]][v[1]])
                if dp[nv[0]][nv[1]] > dp[v[0]][v[1]] + 1 + h:
                    dp[nv[0]][nv[1]] = dp[v[0]][v[1]] + 1 + h
                    q.append(v)
                    q.append(nv)
                    break


def bfs():
    q = deque()
    q.append([0, 0])
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < n:
                h = 0
                if lst[nv[0]][nv[1]] > lst[v[0]][v[1]]:
                    h = lst[nv[0]][nv[1]] - lst[v[0]][v[1]]

                if dp[nv[0]][nv[1]] > dp[v[0]][v[1]] + 1 + h:
                    dp[nv[0]][nv[1]] = dp[v[0]][v[1]] + 1 + h
                    q.append(nv)


ip = int(input())
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    bfs()
    print(f'#{case} {dp[n-1][n-1]}')