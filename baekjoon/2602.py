def dfs(t, x, y):
    if t == nt:
        dp[y][x][t] = 1
        return dp[y][x][t]

    if dp[y][x][t]:
        return dp[y][x][t]

    for i in range(x+1, n+1):
        if lst[y][i-1] == target[t]:
            dp[y][x][t] += dfs(t+1, i, 1-y)
    return dp[y][x][t]


target = list(input())
nt = len(target)
lst = list(list(input()) for _ in range(2))
n = len(lst[0])
ans = 0
dp = [[[0 for _ in range(21)] for _ in range(n+1)] for _ in range(2)]
dfs(0, 0, 0)
dfs(0, 0, 1)
print(dp[0][0][0]+dp[1][0][0])
