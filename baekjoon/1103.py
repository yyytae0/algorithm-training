from sys import setrecursionlimit


def dfs(a, b, cnt):
    if dp[a][b]:
        return dp[a][b]

    for i in way:
        na = a + i[0]*int(lst[a][b])
        nb = b + i[1]*int(lst[a][b])
        if 0 <= na < n and 0 <= nb < m and lst[na][nb] != 'H':
            if visit[na][nb]:
                return -2
            visit[na][nb] = 1
            d = dfs(na, nb, cnt+1)
            if d < 0:
                return -2
            dp[a][b] = max(dp[a][b], d+1)
            visit[na][nb] = 0
    return dp[a][b]


setrecursionlimit(10**5)
n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dp = [[0 for _ in range(m)] for _ in range(n)]
ans = dfs(0, 0, 0)
print(ans+1)
# for i in dp:
#     print(*i)
