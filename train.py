def dfs(t, x, y):
    if t == nt:
        dp[y][x] = 1
        return dp[y][x]

    if dp[y][x]:
        return dp[y][x]

    for i in range(x+1, n+1):
        if lst[y][i-1] == target[t]:
            dp[y][x] += dfs(t+1, i, 1-y)
    return dp[y][x]


target = list(input())
nt = len(target)
lst = list(list(input()) for _ in range(2))
n = len(lst[0])
dp = [[0 for _ in range(n+1)] for _ in range(2)]
dfs(0, 0, 0)
dfs(0, 0, 1)
for i in dp:
    print(*i)
print(dp[0][0]+dp[1][0])
