from sys import setrecursionlimit


def dfs(a, b):
    if dp[a][b]:
        return dp[a][b]
    if a == n-1 and b == m-1:
        return lst[a][b]
    for i in way:
        na, nb = a+i[0], b+i[1]
        if 0 <= na < n and 0 <= nb < m and not visit[na][nb]:
            visit[na][nb] = 1
            dp[a][b] = max(dp[a][b], lst[a][b] + dfs(na, nb))
            visit[na][nb] = 0
    return dp[a][b]


setrecursionlimit(10**6)
n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
way = [[0, 1], [0, -1], [1, 0]]
dp = [[0 for _ in range(m)] for _ in range(n)]

print(dfs(0, 0))
for i in dp:
    print(*i)
print(dp[0][0])
