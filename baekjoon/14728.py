n, t = map(int, input().split())
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for i in range(1, n+1):
    a, b = map(int, input().split())
    for j in range(t+1):
        if j >= a:
            dp[i][j] = max(dp[i-1][j], b, dp[i-1][j-a]+b)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])
